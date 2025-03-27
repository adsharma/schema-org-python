from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class RefundTypeEnumeration(Enumeration):
    """
    Enumerates several kinds of product return refund types.
    """
