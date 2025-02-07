from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.quantitative_value import QuantitativeValue


class BusinessAudience(Audience):
    yearsInOperation: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    yearlyRevenue: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfEmployees: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
