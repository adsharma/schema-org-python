from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from schema_models.day_of_week import DayOfWeek
from schema_models.structured_value import StructuredValue


@dataclass
class OpeningHoursSpecification(StructuredValue):
    """
    The opening hours of a certain place.
    """

    closes: Optional[Union[time, List[time]]] = None
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    opens: Optional[Union[time, List[time]]] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
