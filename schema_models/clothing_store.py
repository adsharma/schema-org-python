from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class ClothingStore(Store):
    """
    A clothing store.
    """
