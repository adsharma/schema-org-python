from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class TelevisionStation(LocalBusiness):
    """
    A television station.
    """
