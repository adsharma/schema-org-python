from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class AdultOrientedEnumeration(Enumeration):
    """
    Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    """
