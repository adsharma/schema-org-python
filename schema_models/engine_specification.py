from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.url import URL


class EngineSpecification(StructuredValue):
    enginePower: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    torque: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    engineType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    engineType: Optional[Union[Text, List[Text]]] = None
    engineType: Optional[Union[URL, List[URL]]] = None
    engineDisplacement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    fuelType: Optional[Union[URL, List[URL]]] = None
    fuelType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    fuelType: Optional[Union[Text, List[Text]]] = None
