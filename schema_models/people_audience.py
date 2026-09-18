from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.medical_condition import MedicalCondition


@dataclass
class PeopleAudience(Audience):
    """
    A set of characteristics belonging to people, e.g. who compose an item's target audience.
    """

    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    requiredGender: Optional[Union[str, List[str]]] = None
    requiredMaxAge: Optional[Union[int, List[int]]] = None
    requiredMinAge: Optional[Union[int, List[int]]] = None
    suggestedAge: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    suggestedGender: Optional[
        Union["GenderType", List["GenderType"], str, List[str]]
    ] = None
    suggestedMaxAge: Optional[Union[float, List[float]]] = None
    suggestedMeasurement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    suggestedMinAge: Optional[Union[float, List[float]]] = None
