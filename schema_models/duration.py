from dataclasses import dataclass

from schema_models.quantity import Quantity


@dataclass
class Duration(Quantity):
    """
    The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    """
