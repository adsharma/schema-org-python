from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class StatusEnumeration(Enumeration):
    """
    Lists or enumerations dealing with status types.
    """
