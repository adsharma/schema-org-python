from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


class Invoice(Intangible):
    billingPeriod: Optional[Union["Duration", List["Duration"]]] = None
    paymentMethodId: Optional[Union[str, List[str]]] = None
    referencesOrder: Optional[Union[Order, List[Order]]] = None
    totalPaymentDue: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    totalPaymentDue: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    paymentMethod: Optional[Union[str, List[str]]] = None
    paymentMethod: Optional[Union["PaymentMethod", List["PaymentMethod"]]] = None
    paymentDue: Optional[Union[datetime, List[datetime]]] = None
    confirmationNumber: Optional[Union[str, List[str]]] = None
    paymentStatus: Optional[Union[str, List[str]]] = None
    paymentStatus: Optional[Union["PaymentStatusType", List["PaymentStatusType"]]] = (
        None
    )
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    accountId: Optional[Union[str, List[str]]] = None
    paymentDueDate: Optional[Union[date, List[date]]] = None
    paymentDueDate: Optional[Union[datetime, List[datetime]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    customer: Optional[Union[Person, List[Person]]] = None
    customer: Optional[Union[Organization, List[Organization]]] = None
    minimumPaymentDue: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    minimumPaymentDue: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    scheduledPaymentDate: Optional[Union[date, List[date]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
