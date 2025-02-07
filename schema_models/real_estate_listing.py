from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.duration import Duration
from schema_models.quantitative_value import QuantitativeValue
from schema_models.web_page import WebPage


class RealEstateListing(WebPage):
    datePosted: Optional[Union[DateTime, List[DateTime]]] = None
    datePosted: Optional[Union[Date, List[Date]]] = None
    leaseLength: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    leaseLength: Optional[Union[Duration, List[Duration]]] = None
