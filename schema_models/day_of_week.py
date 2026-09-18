from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class DayOfWeek(Enumeration):
    """
    The day of the week for which these opening hours are valid.
    """
