from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class OrderStatus(StatusEnumeration):
    """
    The current status of the order.
    """
