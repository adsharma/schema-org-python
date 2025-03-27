from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class TheaterEvent(Event):
    """
    Event type: Theater performance.
    """
