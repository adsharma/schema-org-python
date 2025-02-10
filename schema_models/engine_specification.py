from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


class EngineSpecification(StructuredValue):
    """
    Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.
    """

    enginePower: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    torque: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    engineType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    engineType: Optional[Union[str, List[str]]] = None
    engineType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    engineDisplacement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    fuelType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    fuelType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    fuelType: Optional[Union[str, List[str]]] = None
