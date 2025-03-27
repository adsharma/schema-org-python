from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class RVPark(CivicStructure):
    """
    A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.
    """
