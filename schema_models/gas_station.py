from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class GasStation(AutomotiveBusiness):
    """
    A gas station.
    """
