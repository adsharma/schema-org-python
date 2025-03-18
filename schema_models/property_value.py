from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


class PropertyValue(StructuredValue):
    """
    A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.

     Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

    """

    unitText: Optional[Union[str, List[str]]] = None
    unitCode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    measurementTechnique: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
        ]
    ] = None
    propertyID: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
            str,
            List[str],
        ]
    ] = None
    value: Optional[
        Union[
            bool,
            List[bool],
            str,
            List[str],
            float,
            List[float],
            StructuredValue,
            List[StructuredValue],
        ]
    ] = None
    valueReference: Optional[
        Union[
            str,
            List[str],
            DefinedTerm,
            List[DefinedTerm],
            "PropertyValue",
            List["PropertyValue"],
            MeasurementTypeEnumeration,
            List[MeasurementTypeEnumeration],
            StructuredValue,
            List[StructuredValue],
            Enumeration,
            List[Enumeration],
            QualitativeValue,
            List[QualitativeValue],
            "QuantitativeValue",
            List["QuantitativeValue"],
        ]
    ] = None
    maxValue: Optional[Union[float, List[float]]] = None
