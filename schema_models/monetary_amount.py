from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class MonetaryAmount(StructuredValue):
    maxValue: Optional[Union[float, List[float]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    currency: Optional[Union[str, List[str]]] = None
    value: Optional[Union[bool, List[bool]]] = None
    value: Optional[Union[str, List[str]]] = None
    value: Optional[Union[float, List[float]]] = None
    value: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
