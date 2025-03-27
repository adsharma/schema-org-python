from dataclasses import dataclass

from schema_models.qualitative_value import QualitativeValue


@dataclass
class DriveWheelConfigurationValue(QualitativeValue):
    """
    A value indicating which roadwheels will receive torque.
    """
