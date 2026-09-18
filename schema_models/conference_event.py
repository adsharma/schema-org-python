from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class ConferenceEvent(Event):
    """
    Event type: Conference event.
    """
