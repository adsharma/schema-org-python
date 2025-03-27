from dataclasses import dataclass

from schema_models.size_system_enumeration import SizeSystemEnumeration


@dataclass
class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
    Enumerates common size systems specific for wearable products.
    """
