from dataclasses import dataclass

from schema_models.service import Service


@dataclass
class FoodService(Service):
    """
    A food service, like breakfast, lunch, or dinner.
    """
