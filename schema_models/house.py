from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.accommodation import Accommodation
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue


class House(Accommodation):
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
