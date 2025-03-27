from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class AutoWash(AutomotiveBusiness):
    """
    A car wash business.
    """
