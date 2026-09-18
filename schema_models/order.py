from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.invoice import Invoice
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


@dataclass
class Order(Intangible):
    """
    An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.
    """

    acceptedOffer: Optional[Union[Offer, List[Offer]]] = None
    billingAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    confirmationNumber: Optional[Union[str, List[str]]] = None
    customer: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    discount: Optional[Union[float, List[float], str, List[str]]] = None
    discountCode: Optional[Union[str, List[str]]] = None
    discountCurrency: Optional[Union[str, List[str]]] = None
    isGift: Optional[Union[bool, List[bool]]] = None
    merchant: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    orderDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    orderDelivery: Optional[Union["ParcelDelivery", List["ParcelDelivery"]]] = None
    orderNumber: Optional[Union[str, List[str]]] = None
    orderStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = None
    orderedItem: Optional[
        Union[
            "OrderItem",
            List["OrderItem"],
            Product,
            List[Product],
            "Service",
            List["Service"],
        ]
    ] = None
    partOfInvoice: Optional[Union[Invoice, List[Invoice]]] = None
    paymentDue: Optional[Union[datetime, List[datetime]]] = None
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    paymentMethod: Optional[
        Union["PaymentMethod", List["PaymentMethod"], str, List[str]]
    ] = None
    paymentMethodId: Optional[Union[str, List[str]]] = None
    paymentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
