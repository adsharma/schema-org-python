from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.parcel_delivery import ParcelDelivery
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


@dataclass
class OrderItem(StructuredValue):
    """
    An order item is a line of an order. It includes the quantity and shipping details of a bought offer.
    """

    orderDelivery: Optional[Union[ParcelDelivery, List[ParcelDelivery]]] = None
    orderItemNumber: Optional[Union[str, List[str]]] = None
    orderItemStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = None
    orderQuantity: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    orderedItem: Optional[
        Union[
            "OrderItem",
            List["OrderItem"],
            Product,
            List[Product],
            Service,
            List[Service],
        ]
    ] = None
