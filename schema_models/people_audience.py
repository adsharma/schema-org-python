from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.gender_type import GenderType
from schema_models.integer import Integer
from schema_models.medical_condition import MedicalCondition
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class PeopleAudience(Audience):
    suggestedAge: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    suggestedGender: Optional[Union[GenderType, List[GenderType]]] = None
    suggestedGender: Optional[Union[Text, List[Text]]] = None
    suggestedMeasurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    requiredGender: Optional[Union[Text, List[Text]]] = None
    suggestedMaxAge: Optional[Union[Number, List[Number]]] = None
    requiredMaxAge: Optional[Union[Integer, List[Integer]]] = None
    requiredMinAge: Optional[Union[Integer, List[Integer]]] = None
    suggestedMinAge: Optional[Union[Number, List[Number]]] = None
