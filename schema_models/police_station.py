from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class PoliceStation(CivicStructure):
    """
    A police station.
    """
