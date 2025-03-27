from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class LegalValueLevel(Enumeration):
    """
    A list of possible levels for the legal validity of a legislation.
    """
