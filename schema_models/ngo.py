from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class NGO(Organization):
    """
    Organization: Non-governmental Organization.
    """
