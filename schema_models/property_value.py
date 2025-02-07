from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.number import Number
from schema_models.property_value import PropertyValue
from schema_models.qualitative_value import QualitativeValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.url import URL


class PropertyValue(StructuredValue):
    unitText: Optional[Union[Text, List[Text]]] = None
    unitCode: Optional[Union[Text, List[Text]]] = None
    unitCode: Optional[Union[URL, List[URL]]] = None
    minValue: Optional[Union[Number, List[Number]]] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    propertyID: Optional[Union[Text, List[Text]]] = None
    propertyID: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    value: Optional[Union[Boolean, List[Boolean]]] = None
    value: Optional[Union[Text, List[Text]]] = None
    value: Optional[Union[Number, List[Number]]] = None
    value: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[Text, List[Text]]] = None
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    valueReference: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    valueReference: Optional[
        Union[MeasurementTypeEnumeration, List[MeasurementTypeEnumeration]]
    ] = None
    valueReference: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[Enumeration, List[Enumeration]]] = None
    valueReference: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    valueReference: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    maxValue: Optional[Union[Number, List[Number]]] = None
