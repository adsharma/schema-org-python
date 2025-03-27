from dataclasses import dataclass

from schema_models.food_establishment import FoodEstablishment


@dataclass
class Winery(FoodEstablishment):
    """
    A winery.
    """
