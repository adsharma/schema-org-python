from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


class Order(Intangible):
    """
    An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.
    """

    discountCurrency: Optional[Union[str, List[str]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    orderedItem: Optional[Union["Service", List["Service"]]] = None
    orderedItem: Optional[Union[Product, List[Product]]] = None
    orderedItem: Optional[Union["OrderItem", List["OrderItem"]]] = None
    paymentMethodId: Optional[Union[str, List[str]]] = None
    paymentMethod: Optional[Union[str, List[str]]] = None
    paymentMethod: Optional[Union["PaymentMethod", List["PaymentMethod"]]] = None
    isGift: Optional[Union[bool, List[bool]]] = None
    paymentDue: Optional[Union[datetime, List[datetime]]] = None
    merchant: Optional[Union[Person, List[Person]]] = None
    merchant: Optional[Union[Organization, List[Organization]]] = None
    orderNumber: Optional[Union[str, List[str]]] = None
    acceptedOffer: Optional[Union[Offer, List[Offer]]] = None
    partOfInvoice: Optional[Union["Invoice", List["Invoice"]]] = None
    paymentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    confirmationNumber: Optional[Union[str, List[str]]] = None
    orderDelivery: Optional[Union["ParcelDelivery", List["ParcelDelivery"]]] = None
    orderDate: Optional[Union[date, List[date]]] = None
    orderDate: Optional[Union[datetime, List[datetime]]] = None
    discountCode: Optional[Union[str, List[str]]] = None
    billingAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    discount: Optional[Union[str, List[str]]] = None
    discount: Optional[Union[float, List[float]]] = None
    customer: Optional[Union[Person, List[Person]]] = None
    customer: Optional[Union[Organization, List[Organization]]] = None
    paymentDueDate: Optional[Union[date, List[date]]] = None
    paymentDueDate: Optional[Union[datetime, List[datetime]]] = None
    orderStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
