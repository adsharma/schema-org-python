from dataclasses import dataclass

from schema_models.emergency_service import EmergencyService


@dataclass
class PoliceStation(EmergencyService):
    """
    A police station.
    """
