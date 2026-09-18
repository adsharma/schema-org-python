from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class FoodEvent(Event):
    """
    A sub property of location. The specific food event where the action occurred.
    """
