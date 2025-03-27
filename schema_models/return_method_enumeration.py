from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ReturnMethodEnumeration(Enumeration):
    """
    Enumerates several types of product return methods.
    """
