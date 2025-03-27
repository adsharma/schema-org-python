from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class BikeStore(Store):
    """
    A bike store.
    """
