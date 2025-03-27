from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class AutoRental(AutomotiveBusiness):
    """
    A car rental business.
    """
