from datetime import date, datetime, time
from typing import List, Optional, Union

from schema_models.intangible import Intangible


class Schedule(Intangible):
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    exceptDate: Optional[Union[datetime, List[datetime]]] = None
    exceptDate: Optional[Union[date, List[date]]] = None
    endTime: Optional[Union[datetime, List[datetime]]] = None
    endTime: Optional[Union[time, List[time]]] = None
    repeatFrequency: Optional[Union[str, List[str]]] = None
    repeatFrequency: Optional[Union["Duration", List["Duration"]]] = None
    byMonth: Optional[Union[int, List[int]]] = None
    repeatCount: Optional[Union[int, List[int]]] = None
    byMonthWeek: Optional[Union[int, List[int]]] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    byDay: Optional[Union[str, List[str]]] = None
    byDay: Optional[Union["DayOfWeek", List["DayOfWeek"]]] = None
    byMonthDay: Optional[Union[int, List[int]]] = None
    scheduleTimezone: Optional[Union[str, List[str]]] = None
    startTime: Optional[Union[datetime, List[datetime]]] = None
    startTime: Optional[Union[time, List[time]]] = None
