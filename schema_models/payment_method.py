from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.payment_method_type import PaymentMethodType


class PaymentMethod(Intangible):
    paymentMethodType: Optional[Union[PaymentMethodType, List[PaymentMethodType]]] = (
        None
    )
