from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.delivery_event import DeliveryEvent
from schema_models.intangible import Intangible
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


@dataclass
class ParcelDelivery(Intangible):
    """
    The delivery of a parcel either via the postal service or a commercial service.
    """

    carrier: Optional[Union[Organization, List[Organization]]] = None
    deliveryAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    deliveryStatus: Optional[Union[DeliveryEvent, List[DeliveryEvent]]] = None
    expectedArrivalFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = (
        None
    )
    expectedArrivalUntil: Optional[
        Union[date, List[date], datetime, List[datetime]]
    ] = None
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
    itemShipped: Optional[Union[Product, List[Product]]] = None
    originAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    partOfOrder: Optional[Union[Order, List[Order]]] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    trackingNumber: Optional[Union[str, List[str]]] = None
    trackingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
