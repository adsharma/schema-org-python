from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class OfferItemCondition(Enumeration):
    """
    A list of possible conditions for the item.
    """
