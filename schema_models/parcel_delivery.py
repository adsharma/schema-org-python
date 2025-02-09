from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.delivery_event import DeliveryEvent
from schema_models.intangible import Intangible
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


class ParcelDelivery(Intangible):
    expectedArrivalFrom: Optional[Union[date, List[date]]] = None
    expectedArrivalFrom: Optional[Union[datetime, List[datetime]]] = None
    deliveryAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    carrier: Optional[Union[Organization, List[Organization]]] = None
    itemShipped: Optional[Union[Product, List[Product]]] = None
    deliveryStatus: Optional[Union[DeliveryEvent, List[DeliveryEvent]]] = None
    originAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    trackingNumber: Optional[Union[str, List[str]]] = None
    expectedArrivalUntil: Optional[Union[datetime, List[datetime]]] = None
    expectedArrivalUntil: Optional[Union[date, List[date]]] = None
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    trackingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    partOfOrder: Optional[Union[Order, List[Order]]] = None
