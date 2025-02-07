from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.order_item import OrderItem
from schema_models.order_status import OrderStatus
from schema_models.parcel_delivery import ParcelDelivery
from schema_models.product import Product
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service import Service
from schema_models.text import Text


class OrderItem(Intangible):
    orderDelivery: Optional[Union[ParcelDelivery, List[ParcelDelivery]]] = None
    orderItemStatus: Optional[Union[OrderStatus, List[OrderStatus]]] = None
    orderedItem: Optional[Union[Service, List[Service]]] = None
    orderedItem: Optional[Union[Product, List[Product]]] = None
    orderedItem: Optional[Union["OrderItem", List["OrderItem"]]] = None
    orderQuantity: Optional[Union[Number, List[Number]]] = None
    orderQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    orderItemNumber: Optional[Union[Text, List[Text]]] = None
