from dataclasses import dataclass

from schema_models.vehicle import Vehicle


@dataclass
class MotorizedBicycle(Vehicle):
    """
    A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.
    """
