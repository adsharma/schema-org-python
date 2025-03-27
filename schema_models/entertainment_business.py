from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class EntertainmentBusiness(LocalBusiness):
    """
    A sub property of location. The entertainment business where the action occurred.
    """
