from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.integer import Integer
from schema_models.qualitative_value import QualitativeValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.reservation import Reservation
from schema_models.text import Text
from schema_models.time import Time


class LodgingReservation(Reservation):
    numChildren: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numChildren: Optional[Union[Integer, List[Integer]]] = None
    lodgingUnitDescription: Optional[Union[Text, List[Text]]] = None
    lodgingUnitType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    lodgingUnitType: Optional[Union[Text, List[Text]]] = None
    checkoutTime: Optional[Union[Time, List[Time]]] = None
    checkoutTime: Optional[Union[DateTime, List[DateTime]]] = None
    numAdults: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numAdults: Optional[Union[Integer, List[Integer]]] = None
    checkinTime: Optional[Union[DateTime, List[DateTime]]] = None
    checkinTime: Optional[Union[Time, List[Time]]] = None
