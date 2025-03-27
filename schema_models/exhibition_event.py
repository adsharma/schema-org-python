from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class ExhibitionEvent(Event):
    """
    Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    """
