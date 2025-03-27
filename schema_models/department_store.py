from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class DepartmentStore(Store):
    """
    A department store.
    """
