from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class FireStation(CivicStructure):
    """
    A fire station. With firemen.
    """
