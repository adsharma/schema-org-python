from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.day_of_week import DayOfWeek
from schema_models.structured_value import StructuredValue
from schema_models.time import Time


class OpeningHoursSpecification(StructuredValue):
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
    closes: Optional[Union[Time, List[Time]]] = None
    opens: Optional[Union[Time, List[Time]]] = None
