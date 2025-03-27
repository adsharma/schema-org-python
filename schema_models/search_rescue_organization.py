from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class SearchRescueOrganization(Organization):
    """
    A Search and Rescue organization of some kind.
    """
