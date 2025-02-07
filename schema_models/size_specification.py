from typing import List, Optional, Union

from schema_models.gender_type import GenderType
from schema_models.qualitative_value import QualitativeValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.size_group_enumeration import SizeGroupEnumeration
from schema_models.size_system_enumeration import SizeSystemEnumeration
from schema_models.text import Text


class SizeSpecification(QualitativeValue):
    suggestedAge: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    suggestedGender: Optional[Union[GenderType, List[GenderType]]] = None
    suggestedGender: Optional[Union[Text, List[Text]]] = None
    sizeGroup: Optional[Union[Text, List[Text]]] = None
    sizeGroup: Optional[Union[SizeGroupEnumeration, List[SizeGroupEnumeration]]] = None
    suggestedMeasurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    hasMeasurement: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    sizeSystem: Optional[Union[SizeSystemEnumeration, List[SizeSystemEnumeration]]] = (
        None
    )
    sizeSystem: Optional[Union[Text, List[Text]]] = None
