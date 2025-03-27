from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class PaymentMethodType(Enumeration):
    """
    The type of a payment method.
    """
