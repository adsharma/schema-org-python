from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


@dataclass
class PropertyValue(StructuredValue):
    """
    A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.

     Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

    """

    maxValue: Optional[Union[float, List[float]]] = None
    measurementMethod: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    measurementTechnique: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    minValue: Optional[Union[float, List[float]]] = None
    propertyID: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
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
    valueGroup: Optional[Union[str, List[str]]] = None
    valueReference: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            Enumeration,
            List[Enumeration],
            MeasurementTypeEnumeration,
            List[MeasurementTypeEnumeration],
            "PropertyValue",
            List["PropertyValue"],
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
