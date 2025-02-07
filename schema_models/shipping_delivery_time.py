from typing import List, Optional, Union

from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.time import Time


class ShippingDeliveryTime(StructuredValue):
    businessDays: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    handlingTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    transitTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    cutoffTime: Optional[Union[Time, List[Time]]] = None
