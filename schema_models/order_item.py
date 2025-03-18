from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.product import Product


class OrderItem(Intangible):
    """
    An order item is a line of an order. It includes the quantity and shipping details of a bought offer.
    """

    orderDelivery: Optional[Union["ParcelDelivery", List["ParcelDelivery"]]] = None
    orderItemStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = None
    orderedItem: Optional[
        Union[
            "Service",
            List["Service"],
            Product,
            List[Product],
            "OrderItem",
            List["OrderItem"],
        ]
    ] = None
    orderQuantity: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    orderItemNumber: Optional[Union[str, List[str]]] = None
