from dataclasses import dataclass

from schema_models.food_establishment import FoodEstablishment


@dataclass
class BarOrPub(FoodEstablishment):
    """
    A bar or pub.
    """
