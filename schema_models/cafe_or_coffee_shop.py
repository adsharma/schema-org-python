from dataclasses import dataclass

from schema_models.food_establishment import FoodEstablishment


@dataclass
class CafeOrCoffeeShop(FoodEstablishment):
    """
    A cafe or coffee shop.
    """
