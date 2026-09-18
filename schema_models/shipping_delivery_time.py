from dataclasses import dataclass
from datetime import time
from typing import List, Optional, Union

from schema_models.day_of_week import DayOfWeek
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service_period import ServicePeriod
from schema_models.structured_value import StructuredValue


@dataclass
class ShippingDeliveryTime(StructuredValue):
    """
    ShippingDeliveryTime provides various pieces of information about delivery times for shipping.
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
    handlingTime: Optional[
        Union[
            QuantitativeValue,
            List[QuantitativeValue],
            ServicePeriod,
            List[ServicePeriod],
        ]
    ] = None
    transitTime: Optional[
        Union[
            QuantitativeValue,
            List[QuantitativeValue],
            ServicePeriod,
            List[ServicePeriod],
        ]
    ] = None
