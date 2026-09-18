from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class WarrantyScope(Enumeration):
    """
    The scope of the warranty promise.
    """
