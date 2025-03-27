from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class MovieRentalStore(Store):
    """
    A movie rental store.
    """
