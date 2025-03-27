from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class ChildrensEvent(Event):
    """
    Event type: Children's event.
    """
