from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.integer import Integer
from schema_models.quantitative_value import QuantitativeValue
from schema_models.reservation import Reservation
from schema_models.time import Time


class FoodEstablishmentReservation(Reservation):
    startTime: Optional[Union[DateTime, List[DateTime]]] = None
    startTime: Optional[Union[Time, List[Time]]] = None
    endTime: Optional[Union[DateTime, List[DateTime]]] = None
    endTime: Optional[Union[Time, List[Time]]] = None
    partySize: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    partySize: Optional[Union[Integer, List[Integer]]] = None
