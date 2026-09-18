from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class FulfillmentTypeEnumeration(Enumeration):
    """
    A type of product fulfillment.
    """
