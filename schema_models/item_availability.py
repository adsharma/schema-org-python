from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ItemAvailability(Enumeration):
    """
    A list of possible product availability options.
    """
