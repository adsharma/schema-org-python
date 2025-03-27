from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class JewelryStore(Store):
    """
    A jewelry store.
    """
