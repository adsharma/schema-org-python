from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class PoliticalParty(Organization):
    """
    Organization: Political Party.
    """
