from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class GovernmentBuilding(CivicStructure):
    """
    A government building.
    """
