from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class FurnitureStore(Store):
    """
    A furniture store.
    """
