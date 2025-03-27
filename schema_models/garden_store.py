from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class GardenStore(Store):
    """
    A garden store.
    """
