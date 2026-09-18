from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class IncentiveStatus(Enumeration):
    """
    The status of the incentive (active, on hold, retired, etc.).
    """
