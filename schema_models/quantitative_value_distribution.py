from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.structured_value import StructuredValue


class QuantitativeValueDistribution(StructuredValue):
    duration: Optional[Union[Duration, List[Duration]]] = None
    percentile10: Optional[Union[float, List[float]]] = None
    percentile25: Optional[Union[float, List[float]]] = None
    percentile90: Optional[Union[float, List[float]]] = None
    percentile75: Optional[Union[float, List[float]]] = None
    median: Optional[Union[float, List[float]]] = None
