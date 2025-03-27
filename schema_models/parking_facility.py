from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class ParkingFacility(CivicStructure):
    """
    A parking lot or other parking facility.
    """
