from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


@dataclass
class EngineSpecification(StructuredValue):
    """
    Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.
    """

    engineDisplacement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    enginePower: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    engineType: Optional[
        Union[
            QualitativeValue,
            List[QualitativeValue],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    fuelType: Optional[
        Union[
            QualitativeValue,
            List[QualitativeValue],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    torque: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
