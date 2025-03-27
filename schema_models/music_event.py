from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class MusicEvent(Event):
    """
    Event type: Music event.
    """
