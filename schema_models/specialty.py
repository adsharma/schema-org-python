from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class Specialty(Enumeration):
    """
    Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.
    """
