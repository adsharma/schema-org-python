from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class Consortium(Organization):
    """
    A Consortium is a membership [[Organization]] whose members are typically Organizations.
    """
