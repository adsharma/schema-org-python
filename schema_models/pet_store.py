from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class PetStore(Store):
    """
    A pet store.
    """
