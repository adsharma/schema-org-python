from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


class Invoice(Intangible):
    """
    A statement of the money due for goods or services; a bill.
    """

    billingPeriod: Optional[Union["Duration", List["Duration"]]] = None
    paymentMethodId: Optional[Union[str, List[str]]] = None
    referencesOrder: Optional[Union[Order, List[Order]]] = None
    totalPaymentDue: Optional[
        Union[
            "PriceSpecification",
            List["PriceSpecification"],
            "MonetaryAmount",
            List["MonetaryAmount"],
        ]
    ] = None
    paymentMethod: Optional[
        Union[str, List[str], "PaymentMethod", List["PaymentMethod"]]
    ] = None
    paymentDue: Optional[Union[datetime, List[datetime]]] = None
    confirmationNumber: Optional[Union[str, List[str]]] = None
    paymentStatus: Optional[
        Union[str, List[str], "PaymentStatusType", List["PaymentStatusType"]]
    ] = None
    provider: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    accountId: Optional[Union[str, List[str]]] = None
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    category: Optional[
        Union[
            Thing,
            List[Thing],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            "CategoryCode",
            List["CategoryCode"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    customer: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    minimumPaymentDue: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            "PriceSpecification",
            List["PriceSpecification"],
        ]
    ] = None
    scheduledPaymentDate: Optional[Union[date, List[date]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
