from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class ResearchOrganization(Organization):
    """
    A Research Organization (e.g. scientific institute, research company).
    """
