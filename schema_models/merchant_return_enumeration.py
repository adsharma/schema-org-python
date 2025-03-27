from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MerchantReturnEnumeration(Enumeration):
    """
    Enumerates several kinds of product return policies.
    """
