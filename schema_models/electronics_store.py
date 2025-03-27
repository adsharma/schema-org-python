from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class ElectronicsStore(Store):
    """
    An electronics store.
    """
