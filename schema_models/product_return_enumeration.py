from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ProductReturnEnumeration(Enumeration):
    """
    ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    """
