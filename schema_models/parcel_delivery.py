from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.delivery_event import DeliveryEvent
from schema_models.delivery_method import DeliveryMethod
from schema_models.intangible import Intangible
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.postal_address import PostalAddress
from schema_models.product import Product
from schema_models.text import Text
from schema_models.url import URL


class ParcelDelivery(Intangible):
    expectedArrivalFrom: Optional[Union[Date, List[Date]]] = None
    expectedArrivalFrom: Optional[Union[DateTime, List[DateTime]]] = None
    deliveryAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    carrier: Optional[Union[Organization, List[Organization]]] = None
    itemShipped: Optional[Union[Product, List[Product]]] = None
    deliveryStatus: Optional[Union[DeliveryEvent, List[DeliveryEvent]]] = None
    originAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    trackingNumber: Optional[Union[Text, List[Text]]] = None
    expectedArrivalUntil: Optional[Union[DateTime, List[DateTime]]] = None
    expectedArrivalUntil: Optional[Union[Date, List[Date]]] = None
    hasDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    trackingUrl: Optional[Union[URL, List[URL]]] = None
    partOfOrder: Optional[Union[Order, List[Order]]] = None
