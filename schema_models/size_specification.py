from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.gender_type import GenderType
from schema_models.qualitative_value import QualitativeValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.size_group_enumeration import SizeGroupEnumeration
from schema_models.size_system_enumeration import SizeSystemEnumeration


@dataclass
class SizeSpecification(QualitativeValue):
    """
    Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).
    """

    hasMeasurement: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    sizeGroup: Optional[
        Union[SizeGroupEnumeration, List[SizeGroupEnumeration], str, List[str]]
    ] = None
    sizeSystem: Optional[
        Union[SizeSystemEnumeration, List[SizeSystemEnumeration], str, List[str]]
    ] = None
    suggestedAge: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    suggestedGender: Optional[Union[GenderType, List[GenderType], str, List[str]]] = (
        None
    )
    suggestedMeasurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
