from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class LiteraryEvent(Event):
    """
    Event type: Literary event.
    """
