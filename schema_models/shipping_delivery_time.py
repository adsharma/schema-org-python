from datetime import time
from typing import List, Optional, Union

from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.structured_value import StructuredValue


class ShippingDeliveryTime(StructuredValue):
    """
    ShippingDeliveryTime provides various pieces of information about delivery times for shipping.
    """

    businessDays: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    handlingTime: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    transitTime: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    cutoffTime: Optional[Union[time, List[time]]] = None
