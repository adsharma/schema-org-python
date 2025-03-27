from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class WholesaleStore(Store):
    """
    A wholesale store.
    """
