from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class AutomotiveBusiness(LocalBusiness):
    """
    Car repair, sales, or parts.
    """
