from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class SportsActivityLocation(LocalBusiness):
    """
    A sub property of location. The sports activity location where this action occurred.
    """
