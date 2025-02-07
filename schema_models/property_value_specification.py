from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.text import Text
from schema_models.thing import Thing


class PropertyValueSpecification(Intangible):
    defaultValue: Optional[Union[Thing, List[Thing]]] = None
    defaultValue: Optional[Union[Text, List[Text]]] = None
    stepValue: Optional[Union[Number, List[Number]]] = None
    multipleValues: Optional[Union[Boolean, List[Boolean]]] = None
    valuePattern: Optional[Union[Text, List[Text]]] = None
    valueMinLength: Optional[Union[Number, List[Number]]] = None
    valueRequired: Optional[Union[Boolean, List[Boolean]]] = None
    maxValue: Optional[Union[Number, List[Number]]] = None
    valueMaxLength: Optional[Union[Number, List[Number]]] = None
    readonlyValue: Optional[Union[Boolean, List[Boolean]]] = None
    valueName: Optional[Union[Text, List[Text]]] = None
    minValue: Optional[Union[Number, List[Number]]] = None
