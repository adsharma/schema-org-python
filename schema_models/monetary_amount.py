from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.number import Number
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class MonetaryAmount(StructuredValue):
    maxValue: Optional[Union[Number, List[Number]]] = None
    minValue: Optional[Union[Number, List[Number]]] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    currency: Optional[Union[Text, List[Text]]] = None
    value: Optional[Union[Boolean, List[Boolean]]] = None
    value: Optional[Union[Text, List[Text]]] = None
    value: Optional[Union[Number, List[Number]]] = None
    value: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
