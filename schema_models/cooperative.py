from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class Cooperative(Organization):
    """
    An organization that is a joint project of multiple organizations or persons.
    """
