#!/usr/bin/env python3

import argparse
import os
import re
from collections import defaultdict
from graphlib import TopologicalSorter
from keyword import kwlist
from typing import Dict

import black
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

    # Extract comments into a docstring
    for s, p, o in graph.triples((None, RDFS.comment, None)):
        if str(s).startswith(str(SCHEMA)) and str(s) not in BASE_TYPES_STR:
            class_name = safe_name(str(s).split("/")[-1])
            if class_name in classes:
                classes[class_name]["docstring"] = (
                    o.replace("\\n", "\n")
                    .replace("\\(", "\\\\(")
                    .replace("\\_", "\\\\_")
                )

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

    # Write a tiny lazy __init__.py (PEP 562). Importing any name loads
    # only that module plus its real dependency closure -- never all ~900
    # modules up front, and no eager model_rebuild() cascade. See _lazy.py.
    # NOTE: __init__.py is generated; do not hand-edit it.
    with open("schema_models/__init__.py", "w") as f:
        f.write(
            '"""Schema.org models with lazy loading (see schema_models._lazy)."""\n'
        )
        f.write("\n")
        f.write(
            "from schema_models._lazy import __all__, __getattr__  # noqa: F401,E402\n"
        )

    # Write registry: class -> module map used for lazy loading.
    # _lazy.py supplies each validator() call with its static transitive
    # closure, while the rebuild machinery itself lives in fquery.pydantic.
    with open("schema_models/_registry.py", "w") as f:
        f.write('"""Generated class -> module map. Do not edit."""\n')
        f.write("_MODULE_FOR = {\n")
        for class_name in ts_sorted:
            if class_name is not None:
                class_filename = camel_to_snake(class_name)
                f.write(f'    "{class_name}": "{class_filename}",\n')
        f.write("}\n")

    # Write static transitive reference closures for validator namespaces.
    # NOTE: properties are collected in the second pass below, so this
    # runs after model files are generated (see end of generate_models).
    def _write_namespaces():
        direct = {}
        for class_name, class_info in classes.items():
            deps = set()
            if class_info["parent"] and class_info["parent"] in classes:
                deps.add(class_info["parent"])
            for _, prop_type in class_info["properties"]:
                if prop_type in classes:
                    deps.add(prop_type)
            direct[class_name] = deps
        with open("schema_models/_namespaces.py", "w") as f:
            f.write('"""Generated transitive reference closures. Do not edit."""\n')
            f.write("_NAMESPACES = {\n")
            for class_name in sorted(direct):
                seen, stack = set(), list(direct[class_name])
                while stack:
                    dep = stack.pop()
                    if dep in seen:
                        continue
                    seen.add(dep)
                    stack.extend(direct.get(dep, set()) - seen)
                seen.discard(class_name)
                f.write(f'    "{class_name}": {tuple(sorted(seen))},\n')
            f.write("}\n")

    _write_namespaces_later = _write_namespaces

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
                        prop_name = f"{prop_name}_"
                    class_info["properties"].append((prop_name, python_type))
                except Exception:
                    pass

    # Generate model files. Imports are emitted already isort-clean
    # (stdlib, third-party, first-party; alphabetical; only what is used)
    # and each file is formatted in-process with black, so no post-pass
    # over ~900 files is needed.
    mode = black.Mode()
    for class_name, class_info in classes.items():
        filename = f"schema_models/{camel_to_snake(class_name)}.py"

        # Import other classes
        other_classes = {}
        for prop_name, prop_type in class_info["properties"]:
            if (
                prop_type != class_name
                and prop_type != class_info["parent"]
                and prop_type not in BASE_TYPES.values()
            ):
                forward_def = classes[prop_type]["order"] > class_info["order"]
                other_classes[prop_type] = forward_def

        prop_dict = defaultdict(list)
        for prop_name, prop_type in class_info["properties"]:
            # if prop_type is self, it should be in double quotes
            forward_def = other_classes.get(prop_type, False)
            if prop_type == class_name or forward_def:
                prop_type = f'"{prop_type}"'
            prop_dict[prop_name].append(prop_type)

        used = {t.strip('"') for types in prop_dict.values() for t in types}
        need_typing = bool(prop_dict)
        need_http_url = "HttpUrl" in used
        need_datetime = sorted({t for t in ("date", "datetime", "time") if t in used})
        is_subclass = bool(class_info["parent"])

        lines = []
        if is_subclass:
            lines.append("from dataclasses import dataclass")
        if need_datetime:
            lines.append(f"from datetime import {', '.join(need_datetime)}")
        if need_typing:
            lines.append("from typing import List, Optional, Union")
        if lines:
            lines.append("")
        if class_name == "Thing":
            lines.append("from fquery.pydantic import pydantic")
        if need_http_url:
            lines.append("from pydantic import HttpUrl")
        if class_name == "Thing" or need_http_url:
            lines.append("")
        first_party = []
        if class_info["parent"]:
            parent = camel_to_snake(class_info["parent"])
            first_party.append(
                f"from schema_models.{parent} import {class_info['parent']}"
            )
        for prop_type in sorted(other_classes):
            if not other_classes[prop_type]:
                first_party.append(
                    f"from schema_models.{camel_to_snake(prop_type)} import {prop_type}"
                )
        lines.extend(sorted(first_party))
        if first_party:
            lines.append("")
        lines.append("")

        # Class definition
        if is_subclass:
            # Use the @dataclass decorator for subclasses
            # Using @pydantic decorator results in a deep recursion
            # and slow startup
            lines.append("@dataclass")
            lines.append(f"class {class_name}({class_info['parent']}):")
        else:
            if class_name == "Thing":
                lines.append("@pydantic")
            lines.append(f"class {class_name}:")
        docstring = class_info.get("docstring", None)
        if docstring is not None:
            lines.append(f'    """\n{docstring}\n    """')

        # Properties
        if not class_info["properties"] and docstring is None:
            lines.append("    pass")

        for prop_name, prop_type_list in prop_dict.items():
            prop_types = ", ".join(
                [f"{prop_type}, List[{prop_type}]" for prop_type in prop_type_list]
            )
            lines.append(f"    {prop_name}: Optional[Union[{prop_types}]] = None")

        src = "\n".join(lines).rstrip("\n") + "\n"
        with open(filename, "w") as f:
            f.write(black.format_str(src, mode=mode))

    for s in BASE_TYPES_STR:
        class_name = safe_name(s.split("/")[-1])
        filename = f"schema_models/{camel_to_snake(class_name)}.py"
        src = (
            "from fquery.pydantic import pydantic\n\n\n"
            "@pydantic\n"
            f"class {class_name}:\n"
            "    pass\n"
        )
        with open(filename, "w") as f:
            f.write(black.format_str(src, mode=mode))
    # Properties are complete now: emit static validator namespaces.
    _write_namespaces_later()
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
