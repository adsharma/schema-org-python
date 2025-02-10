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
    unitCode: Optional[Union[str, List[str]]] = None
    unitCode: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    measurementTechnique: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    propertyID: Optional[Union[str, List[str]]] = None
    propertyID: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[str, List[str]]] = None
    value: Optional[Union[bool, List[bool]]] = None
    value: Optional[Union[str, List[str]]] = None
    value: Optional[Union[float, List[float]]] = None
    value: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[str, List[str]]] = None
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    valueReference: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    valueReference: Optional[
        Union[MeasurementTypeEnumeration, List[MeasurementTypeEnumeration]]
    ] = None
    valueReference: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[Enumeration, List[Enumeration]]] = None
    valueReference: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    valueReference: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    maxValue: Optional[Union[float, List[float]]] = None
