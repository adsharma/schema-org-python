from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.product import Product
from schema_models.text import Text


class OrderItem(Intangible):
    orderDelivery: Optional[Union["ParcelDelivery", List["ParcelDelivery"]]] = None
    orderItemStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = None
    orderedItem: Optional[Union["Service", List["Service"]]] = None
    orderedItem: Optional[Union[Product, List[Product]]] = None
    orderedItem: Optional[Union["OrderItem", List["OrderItem"]]] = None
    orderQuantity: Optional[Union[Number, List[Number]]] = None
    orderQuantity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    orderItemNumber: Optional[Union[Text, List[Text]]] = None
