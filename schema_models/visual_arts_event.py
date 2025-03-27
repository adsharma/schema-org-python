from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class VisualArtsEvent(Event):
    """
    Event type: Visual arts event.
    """
