from dataclasses import dataclass

from schema_models.size_group_enumeration import SizeGroupEnumeration


@dataclass
class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """
    Enumerates common size groups (also known as "size types") for wearable products.
    """
