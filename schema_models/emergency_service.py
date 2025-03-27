from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class EmergencyService(LocalBusiness):
    """
    An emergency service, such as a fire station or ER.
    """
