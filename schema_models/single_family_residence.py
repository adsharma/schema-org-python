from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.house import House
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue


class SingleFamilyResidence(House):
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
