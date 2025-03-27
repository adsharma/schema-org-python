from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class Festival(Event):
    """
    Event type: Festival.
    """
