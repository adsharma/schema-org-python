from datetime import date, datetime, time
from typing import List, Optional, Union

from schema_models.day_of_week import DayOfWeek
from schema_models.structured_value import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
    closes: Optional[Union[time, List[time]]] = None
    opens: Optional[Union[time, List[time]]] = None
