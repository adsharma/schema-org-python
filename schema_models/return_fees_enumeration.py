from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ReturnFeesEnumeration(Enumeration):
    """
    Enumerates several kinds of policies for product return fees.
    """
