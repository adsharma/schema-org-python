from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.quantitative_value import QuantitativeValue
from schema_models.thing import Thing


class StupidType(Thing):
    stupidProperty: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
