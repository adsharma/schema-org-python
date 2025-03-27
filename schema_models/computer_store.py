from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class ComputerStore(Store):
    """
    A computer store.
    """
