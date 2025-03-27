from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class FoodEvent(Event):
    """
    Event type: Food event.
    """
