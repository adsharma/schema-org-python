#!/usr/bin/env python3

import argparse
import os
import re
from graphlib import TopologicalSorter
from keyword import kwlist
from typing import Dict

import requests
from rdflib import RDF, RDFS, Graph, Namespace

SCHEMA = Namespace("https://schema.org/")
BASE_TYPES = {
    SCHEMA.Text: "str",
    SCHEMA.Number: "float",
    SCHEMA.Integer: "int",
    SCHEMA.Float: "float",
    SCHEMA.Boolean: "bool",
    SCHEMA.Date: "date",
    SCHEMA.DateTime: "datetime",
    SCHEMA.Time: "time",
    SCHEMA.URL: "HttpUrl",
    SCHEMA.XPathType: "str",
    SCHEMA.DataType: "str",
}
BASE_TYPES_STR = {str(k) for k in BASE_TYPES.keys()}


def fetch_schema():
    url = "https://schema.org/version/latest/schemaorg-all-https.nt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_schema(content: str) -> Graph:
    g = Graph()
    g.parse(data=content, format="nt")
    return g


def safe_name(name: str) -> str:
    clean_name = re.sub(r"[^a-zA-Z0-9]", "", name)
    return clean_name[0].upper() + clean_name[1:]


def get_parent_class(graph: Graph, class_uri):
    for _, _, parent_uri in graph.triples((class_uri, RDFS.subClassOf, None)):
        if str(parent_uri).startswith(str(SCHEMA)):
            return safe_name(str(parent_uri).split("/")[-1])
    return None


def camel_to_snake(name):
    # Insert underscores before capital letters and lowercase the string
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscores before capital letters followed by lowercase letters
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    # Convert the entire string to lowercase
    return s2.lower()


def generate_models(graph: Graph):
    os.makedirs("schema_models", exist_ok=True)

    classes: Dict[str, Dict] = {}

    # First pass: collect class info
    for s, p, o in graph.triples((None, RDF.type, RDFS.Class)):
        if str(s).startswith(str(SCHEMA)) and str(s) not in BASE_TYPES_STR:
            class_name = safe_name(str(s).split("/")[-1])
            parent_class = get_parent_class(graph, s)
            classes[class_name] = {"parent": parent_class, "properties": []}

    # if class_name begins with a number, add underscore to the class name
    deleted_keys = set()
    for class_name, class_info in classes.items():
        if class_name[0].isdigit() or class_name.lower() in kwlist:
            deleted_keys.add(class_name)

    for class_name in deleted_keys:
        classes[f"_{class_name}"] = classes[class_name]
        del classes[class_name]

    ts = TopologicalSorter()
    ts_sorted = []
    for class_name, class_info in classes.items():
        parent = class_info["parent"]
        ts.add(class_name, parent)
    for order, class_name in enumerate(ts.static_order()):
        if class_name is not None and class_name in classes:
            classes[class_name]["order"] = order
            ts_sorted.append(class_name)

    # Write init file
    with open("schema_models/__init__.py", "w") as f:
        f.write("from typing import Union, List, Optional\n")
        f.write("from datetime import date, datetime, time\n")
        f.write("from pydantic import field_validator, ConfigDict, Field, HttpUrl\n\n")

        for class_name in ts_sorted:
            if class_name is not None:
                class_filename = camel_to_snake(class_name)
                f.write(f"from schema_models.{class_filename} import {class_name}\n")

        f.write("\n\n")

        for class_name in ts_sorted:
            if class_name is not None:
                f.write(f"{class_name}.__pydantic__.model_rebuild()\n")

    # Second pass: collect properties
    for class_name, class_info in classes.items():
        class_uri = SCHEMA[class_name]

        for s, p, o in graph.triples((None, SCHEMA.domainIncludes, class_uri)):
            prop_name = str(s).split("/")[-1]

            for _, _, prop_range in graph.triples((s, SCHEMA.rangeIncludes, None)):
                try:
                    if prop_range in BASE_TYPES:
                        python_type = BASE_TYPES[prop_range]
                    else:
                        python_type = safe_name(str(prop_range).split("/")[-1])
                    # if class_name begins with a number, add underscore to the class name
                    if python_type[0].isdigit() or python_type.lower() in kwlist:
                        python_type = f"_{python_type}"
                    # Ditto for property names
                    if prop_name[0].isdigit() or prop_name.lower() in kwlist:
                        prop_name = f"_{prop_name}"
                    class_info["properties"].append((prop_name, python_type))
                except Exception:
                    pass

    # Generate model files
    for class_name, class_info in classes.items():
        filename = f"schema_models/{camel_to_snake(class_name)}.py"
        with open(filename, "w") as f:
            # Imports
            f.write("from typing import Union, List, Optional\n")
            f.write("from datetime import date, datetime, time\n")
            f.write(
                "from pydantic import field_validator, ConfigDict, Field, HttpUrl\n"
            )

            # Import parent class if exists
            if class_info["parent"]:
                parent = camel_to_snake(class_info["parent"])
                f.write(
                    f"from schema_models.{parent} import {class_info['parent']}\n\n"
                )
            else:
                f.write("\n")

            # Import other classes
            other_classes = {}
            for prop_name, prop_type in class_info["properties"]:
                if prop_type != class_name and prop_type not in BASE_TYPES.values():
                    forward_def = classes[prop_type]["order"] > class_info["order"]
                    other_classes[prop_type] = forward_def

            for prop_type, forward_def in other_classes.items():
                other_snake = camel_to_snake(prop_type)
                if not forward_def:
                    f.write(f"from schema_models.{other_snake} import {prop_type}\n")
            f.write("\n")

            # Class definition
            if class_info["parent"]:
                f.write(f"class {class_name}({class_info['parent']}):\n")
            else:
                if class_name == "Thing":
                    f.write("from fquery.pydantic import pydantic\n\n")
                    f.write("@pydantic\n")
                f.write(f"class {class_name}:\n")

            # f.write("    model_config = ConfigDict(arbitrary_types_allowed=True)\n\n")

            # Properties
            if not class_info["properties"]:
                f.write("    pass\n")

            for prop_name, prop_type in class_info["properties"]:
                # if prop_type is self, it should be in double quotes
                forward_def = other_classes.get(prop_type, False)
                if prop_type == class_name or forward_def:
                    prop_type = f'"{prop_type}"'
                f.write(
                    f"    {prop_name}: Optional[Union[{prop_type}, List[{prop_type}]]] = None\n"
                )

    for s in BASE_TYPES_STR:
        class_name = safe_name(s.split("/")[-1])
        filename = f"schema_models/{camel_to_snake(class_name)}.py"
        with open(filename, "w") as f:
            f.write("from fquery.pydantic import pydantic\n\n")
            f.write("@pydantic\n")
            f.write(f"class {class_name}:\n")
            f.write("    pass\n")
    return classes


def main():
    # print("Fetching Schema.org definitions...")
    # content = fetch_schema()

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Generate pydantic models from schema.org"
    )

    # Add arguments
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    # Parse arguments
    args, rest = parser.parse_known_args()

    if len(rest) != 1:
        print("Need exactly one argument")

    content = open(rest[0]).read()

    print("Parsing RDF data...")
    graph = parse_schema(content)

    print("Generating Pydantic models...")
    generate_models(graph)

    print("Models generated in schema_models directory")


if __name__ == "__main__":
    main()
