from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class RestrictedDiet(Enumeration):
    """
    A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.
    """
