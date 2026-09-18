from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.property_value import PropertyValue
from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


@dataclass
class QuantitativeValue(StructuredValue):
    """
    A point value or interval for product characteristics and other purposes.
    """

    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    maxValue: Optional[Union[float, List[float]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    unitCode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    unitText: Optional[Union[str, List[str]]] = None
    value: Optional[
        Union[
            bool,
            List[bool],
            float,
            List[float],
            QualitativeValue,
            List[QualitativeValue],
            StructuredValue,
            List[StructuredValue],
            str,
            List[str],
        ]
    ] = None
    valueReference: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            Enumeration,
            List[Enumeration],
            MeasurementTypeEnumeration,
            List[MeasurementTypeEnumeration],
            PropertyValue,
            List[PropertyValue],
            QualitativeValue,
            List[QualitativeValue],
            "QuantitativeValue",
            List["QuantitativeValue"],
            StructuredValue,
            List[StructuredValue],
            str,
            List[str],
        ]
    ] = None
