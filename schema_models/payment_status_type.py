from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class PaymentStatusType(StatusEnumeration):
    """
    A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
