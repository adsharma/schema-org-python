from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class PriceComponentTypeEnumeration(Enumeration):
    """
    Enumerates different price components that together make up the total price for an offered product.
    """
