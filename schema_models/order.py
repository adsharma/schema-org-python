from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.invoice import Invoice
from schema_models.number import Number
from schema_models.offer import Offer
from schema_models.order_item import OrderItem
from schema_models.order_status import OrderStatus
from schema_models.organization import Organization
from schema_models.parcel_delivery import ParcelDelivery
from schema_models.payment_method import PaymentMethod
from schema_models.person import Person
from schema_models.postal_address import PostalAddress
from schema_models.product import Product
from schema_models.service import Service
from schema_models.text import Text
from schema_models.url import URL


class Order(Intangible):
    discountCurrency: Optional[Union[Text, List[Text]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    orderedItem: Optional[Union[Service, List[Service]]] = None
    orderedItem: Optional[Union[Product, List[Product]]] = None
    orderedItem: Optional[Union[OrderItem, List[OrderItem]]] = None
    paymentMethodId: Optional[Union[Text, List[Text]]] = None
    paymentMethod: Optional[Union[Text, List[Text]]] = None
    paymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = None
    isGift: Optional[Union[Boolean, List[Boolean]]] = None
    paymentDue: Optional[Union[DateTime, List[DateTime]]] = None
    merchant: Optional[Union[Person, List[Person]]] = None
    merchant: Optional[Union[Organization, List[Organization]]] = None
    orderNumber: Optional[Union[Text, List[Text]]] = None
    acceptedOffer: Optional[Union[Offer, List[Offer]]] = None
    partOfInvoice: Optional[Union[Invoice, List[Invoice]]] = None
    paymentUrl: Optional[Union[URL, List[URL]]] = None
    confirmationNumber: Optional[Union[Text, List[Text]]] = None
    orderDelivery: Optional[Union[ParcelDelivery, List[ParcelDelivery]]] = None
    orderDate: Optional[Union[Date, List[Date]]] = None
    orderDate: Optional[Union[DateTime, List[DateTime]]] = None
    discountCode: Optional[Union[Text, List[Text]]] = None
    billingAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    discount: Optional[Union[Text, List[Text]]] = None
    discount: Optional[Union[Number, List[Number]]] = None
    customer: Optional[Union[Person, List[Person]]] = None
    customer: Optional[Union[Organization, List[Organization]]] = None
    paymentDueDate: Optional[Union[Date, List[Date]]] = None
    paymentDueDate: Optional[Union[DateTime, List[DateTime]]] = None
    orderStatus: Optional[Union[OrderStatus, List[OrderStatus]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
