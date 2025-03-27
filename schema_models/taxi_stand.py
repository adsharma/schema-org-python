from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class TaxiStand(CivicStructure):
    """
    A taxi stand.
    """
