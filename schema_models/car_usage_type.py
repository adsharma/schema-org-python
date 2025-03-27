from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class CarUsageType(Enumeration):
    """
    A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """
