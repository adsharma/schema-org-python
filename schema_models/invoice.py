from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.category_code import CategoryCode
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.monetary_amount import MonetaryAmount
from schema_models.order import Order
from schema_models.organization import Organization
from schema_models.payment_method import PaymentMethod
from schema_models.payment_status_type import PaymentStatusType
from schema_models.person import Person
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Invoice(Intangible):
    billingPeriod: Optional[Union[Duration, List[Duration]]] = None
    paymentMethodId: Optional[Union[Text, List[Text]]] = None
    referencesOrder: Optional[Union[Order, List[Order]]] = None
    totalPaymentDue: Optional[Union[PriceSpecification, List[PriceSpecification]]] = (
        None
    )
    totalPaymentDue: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    paymentMethod: Optional[Union[Text, List[Text]]] = None
    paymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = None
    paymentDue: Optional[Union[DateTime, List[DateTime]]] = None
    confirmationNumber: Optional[Union[Text, List[Text]]] = None
    paymentStatus: Optional[Union[Text, List[Text]]] = None
    paymentStatus: Optional[Union[PaymentStatusType, List[PaymentStatusType]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    accountId: Optional[Union[Text, List[Text]]] = None
    paymentDueDate: Optional[Union[Date, List[Date]]] = None
    paymentDueDate: Optional[Union[DateTime, List[DateTime]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    customer: Optional[Union[Person, List[Person]]] = None
    customer: Optional[Union[Organization, List[Organization]]] = None
    minimumPaymentDue: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    minimumPaymentDue: Optional[Union[PriceSpecification, List[PriceSpecification]]] = (
        None
    )
    scheduledPaymentDate: Optional[Union[Date, List[Date]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
