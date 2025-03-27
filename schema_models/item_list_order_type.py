from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ItemListOrderType(Enumeration):
    """
    Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
