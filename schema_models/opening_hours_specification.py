from datetime import date, datetime, time
from typing import List, Optional, Union

from schema_models.day_of_week import DayOfWeek
from schema_models.structured_value import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    """
    A structured value providing information about the opening hours of a place or a certain service inside a place.


    The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.

    If the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.

    """

    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
    closes: Optional[Union[time, List[time]]] = None
    opens: Optional[Union[time, List[time]]] = None
