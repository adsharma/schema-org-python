from dataclasses import dataclass
from datetime import time
from typing import List, Optional, Union

from schema_models.day_of_week import DayOfWeek
from schema_models.duration import Duration
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue


@dataclass
class ServicePeriod(StructuredValue):
    """
    ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time.
    """

    businessDays: Optional[
        Union[
            DayOfWeek,
            List[DayOfWeek],
            OpeningHoursSpecification,
            List[OpeningHoursSpecification],
        ]
    ] = None
    cutoffTime: Optional[Union[time, List[time]]] = None
    duration: Optional[
        Union[Duration, List[Duration], QuantitativeValue, List[QuantitativeValue]]
    ] = None
