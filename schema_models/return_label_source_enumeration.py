from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class ReturnLabelSourceEnumeration(Enumeration):
    """
    Enumerates several types of return labels for product returns.
    """
