from dataclasses import dataclass

from schema_models.qualitative_value import QualitativeValue


@dataclass
class BedType(QualitativeValue):
    """
    A type of bed. This is used for indicating the bed or beds available in an accommodation.
    """
