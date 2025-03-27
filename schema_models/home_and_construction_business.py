from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class HomeAndConstructionBusiness(LocalBusiness):
    """
    A construction business.

    A HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.

    As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    """
