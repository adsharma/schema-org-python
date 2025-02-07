from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.property_value import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
