from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class GenderType(Enumeration):
    """
    An enumeration of genders.
    """
