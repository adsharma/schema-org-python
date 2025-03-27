from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class EventVenue(CivicStructure):
    """
    An event venue.
    """
