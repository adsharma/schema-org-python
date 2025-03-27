from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class ConvenienceStore(Store):
    """
    A convenience store.
    """
