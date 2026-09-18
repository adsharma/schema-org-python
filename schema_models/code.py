from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Code(CreativeWork):
    """
    A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
    """
