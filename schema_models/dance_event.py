from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class DanceEvent(Event):
    """
    Event type: A social dance.
    """
