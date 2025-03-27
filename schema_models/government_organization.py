from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class GovernmentOrganization(Organization):
    """
    A governmental organization or agency.
    """
