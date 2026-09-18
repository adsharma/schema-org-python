from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class PaymentMethod(Intangible):
    """
    The name of the credit card or other method of payment for the order.
    """

    paymentMethodType: Optional[
        Union["PaymentMethodType", List["PaymentMethodType"]]
    ] = None
