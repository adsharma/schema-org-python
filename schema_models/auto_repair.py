from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class AutoRepair(AutomotiveBusiness):
    """
    Car repair business.
    """
