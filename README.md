# Pydantic models for schema.org

[Schema.org](schema.org) is a community-driven vocabulary that allows users to add structured data to content on the web. It's used by webmasters to help search engines understand web pages. Knowledge graphs such as yago also use schema.org to enforce semantics on wikidata.

Pydantic is the most widely used data validation library for Python.

This project includes a [script](create_pydantic.py) that converts the schema defined in N-Triples(nt) format into a pydantic object. These objects can be used to validate any input data for conformance.

The inheritance hierarchy of the schema is accurately reflected in the python inheritance hierarchy.

Usage:

```
wget https://schema.org/version/latest/schemaorg-all-https.nt
./create_pydantic.py schemaorg-all-https.nt
pytest
```

One time setup:

```
pre-commit install
```

Schemas are provided under the following [license](https://schema.org/docs/terms.html).
