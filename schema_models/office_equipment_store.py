from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class OfficeEquipmentStore(Store):
    """
    An office equipment store.
    """
