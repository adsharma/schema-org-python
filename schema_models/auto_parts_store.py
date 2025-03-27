from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class AutoPartsStore(Store):
    """
    An auto parts store.
    """
