from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class ComedyEvent(Event):
    """
    Event type: Comedy event.
    """
