from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class GroceryStore(Store):
    """
    A grocery store.
    """
