from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class MusicStore(Store):
    """
    A music store.
    """
