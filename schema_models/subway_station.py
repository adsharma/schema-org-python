from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class SubwayStation(CivicStructure):
    """
    A subway station.
    """
