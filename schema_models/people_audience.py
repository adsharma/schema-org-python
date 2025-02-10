from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.gender_type import GenderType
from schema_models.medical_condition import MedicalCondition
from schema_models.quantitative_value import QuantitativeValue


class PeopleAudience(Audience):
    """
    A set of characteristics belonging to people, e.g. who compose an item's target audience.
    """

    suggestedAge: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    suggestedGender: Optional[Union[GenderType, List[GenderType]]] = None
    suggestedGender: Optional[Union[str, List[str]]] = None
    suggestedMeasurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    requiredGender: Optional[Union[str, List[str]]] = None
    suggestedMaxAge: Optional[Union[float, List[float]]] = None
    requiredMaxAge: Optional[Union[int, List[int]]] = None
    requiredMinAge: Optional[Union[int, List[int]]] = None
    suggestedMinAge: Optional[Union[float, List[float]]] = None
