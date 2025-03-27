from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class SizeGroupEnumeration(Enumeration):
    """
    Enumerates common size groups for various product categories.
    """
