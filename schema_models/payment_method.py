from typing import List, Optional, Union

from schema_models.intangible import Intangible


class PaymentMethod(Intangible):
    paymentMethodType: Optional[
        Union["PaymentMethodType", List["PaymentMethodType"]]
    ] = None
