from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.property_value import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
