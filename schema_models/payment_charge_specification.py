from typing import List, Optional, Union

from schema_models.delivery_method import DeliveryMethod
from schema_models.payment_method import PaymentMethod
from schema_models.price_specification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """
    The costs of settling the payment using a particular payment method.
    """

    appliesToPaymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = None
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
