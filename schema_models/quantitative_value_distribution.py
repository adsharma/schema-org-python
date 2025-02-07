from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.duration import Duration
from schema_models.number import Number
from schema_models.structured_value import StructuredValue


class QuantitativeValueDistribution(StructuredValue):
    duration: Optional[Union[Duration, List[Duration]]] = None
    percentile10: Optional[Union[Number, List[Number]]] = None
    percentile25: Optional[Union[Number, List[Number]]] = None
    percentile90: Optional[Union[Number, List[Number]]] = None
    percentile75: Optional[Union[Number, List[Number]]] = None
    median: Optional[Union[Number, List[Number]]] = None
