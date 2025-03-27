from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class PlaceOfWorship(CivicStructure):
    """
    Place of worship, such as a church, synagogue, or mosque.
    """
