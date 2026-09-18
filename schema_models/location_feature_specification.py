from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.property_value import PropertyValue


@dataclass
class LocationFeatureSpecification(PropertyValue):
    """
    Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.
    """

    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
