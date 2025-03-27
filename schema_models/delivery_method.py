from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class DeliveryMethod(Enumeration):
    """
    A sub property of instrument. The method of delivery.
    """
