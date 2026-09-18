from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


@dataclass
class Invoice(Intangible):
    """
    A statement of the money due for goods or services; a bill.
    """

    accountId: Optional[Union[str, List[str]]] = None
    billingPeriod: Optional[Union[Duration, List[Duration]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    category: Optional[
        Union[
            "CategoryCode",
            List["CategoryCode"],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            str,
            List[str],
            Thing,
            List[Thing],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    confirmationNumber: Optional[Union[str, List[str]]] = None
    customer: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    minimumPaymentDue: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            "PriceSpecification",
            List["PriceSpecification"],
        ]
    ] = None
    paymentDue: Optional[Union[datetime, List[datetime]]] = None
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    paymentMethod: Optional[
        Union["PaymentMethod", List["PaymentMethod"], str, List[str]]
    ] = None
    paymentMethodId: Optional[Union[str, List[str]]] = None
    paymentStatus: Optional[
        Union["PaymentStatusType", List["PaymentStatusType"], str, List[str]]
    ] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    referencesOrder: Optional[Union["Order", List["Order"]]] = None
    scheduledPaymentDate: Optional[Union[date, List[date]]] = None
    totalPaymentDue: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            "PriceSpecification",
            List["PriceSpecification"],
        ]
    ] = None
