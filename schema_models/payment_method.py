from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.payment_method_type import PaymentMethodType


class PaymentMethod(Intangible):
    paymentMethodType: Optional[Union[PaymentMethodType, List[PaymentMethodType]]] = (
        None
    )
