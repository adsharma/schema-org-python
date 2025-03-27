from dataclasses import dataclass

from schema_models.food_establishment import FoodEstablishment


@dataclass
class IceCreamShop(FoodEstablishment):
    """
    An ice cream shop.
    """
