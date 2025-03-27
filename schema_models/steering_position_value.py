from dataclasses import dataclass

from schema_models.qualitative_value import QualitativeValue


@dataclass
class SteeringPositionValue(QualitativeValue):
    """
    A value indicating a steering position.
    """
