from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.vehicle import Vehicle


class Car(Vehicle):
    acrissCode: Optional[Union[Text, List[Text]]] = None
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
