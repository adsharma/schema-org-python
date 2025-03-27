from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class ShoeStore(Store):
    """
    A shoe store.
    """
