from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class BusinessEvent(Event):
    """
    Event type: Business event.
    """
