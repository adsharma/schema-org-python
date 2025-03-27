from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class MotorcycleRepair(AutomotiveBusiness):
    """
    A motorcycle repair shop.
    """
