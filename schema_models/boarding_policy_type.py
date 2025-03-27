from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class BoardingPolicyType(Enumeration):
    """
    A type of boarding policy used by an airline.
    """
