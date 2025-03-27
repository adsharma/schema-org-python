from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class OutletStore(Store):
    """
    An outlet store.
    """
