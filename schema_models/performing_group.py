from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class PerformingGroup(Organization):
    """
    A performance group, such as a band, an orchestra, or a circus.
    """
