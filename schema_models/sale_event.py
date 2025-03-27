from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class SaleEvent(Event):
    """
    Event type: Sales event.
    """
