from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.day_of_week import DayOfWeek
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.text import Text
from schema_models.time import Time


class Schedule(Intangible):
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    exceptDate: Optional[Union[DateTime, List[DateTime]]] = None
    exceptDate: Optional[Union[Date, List[Date]]] = None
    endTime: Optional[Union[DateTime, List[DateTime]]] = None
    endTime: Optional[Union[Time, List[Time]]] = None
    repeatFrequency: Optional[Union[Text, List[Text]]] = None
    repeatFrequency: Optional[Union[Duration, List[Duration]]] = None
    byMonth: Optional[Union[Integer, List[Integer]]] = None
    repeatCount: Optional[Union[Integer, List[Integer]]] = None
    byMonthWeek: Optional[Union[Integer, List[Integer]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    duration: Optional[Union[Duration, List[Duration]]] = None
    byDay: Optional[Union[Text, List[Text]]] = None
    byDay: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    byMonthDay: Optional[Union[Integer, List[Integer]]] = None
    scheduleTimezone: Optional[Union[Text, List[Text]]] = None
    startTime: Optional[Union[DateTime, List[DateTime]]] = None
    startTime: Optional[Union[Time, List[Time]]] = None
