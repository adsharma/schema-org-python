from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MeasurementMethodEnum(Enumeration):
    """
    Enumeration(s) for use with [[measurementMethod]].
    """
