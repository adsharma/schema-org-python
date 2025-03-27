from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class HardwareStore(Store):
    """
    A hardware store.
    """
