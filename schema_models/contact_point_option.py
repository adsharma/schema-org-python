from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ContactPointOption(Enumeration):
    """
    Enumerated options related to a ContactPoint.
    """
