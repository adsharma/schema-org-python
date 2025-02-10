from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.property_value import PropertyValue
from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


class QuantitativeValue(StructuredValue):
    """
    A point value or interval for product characteristics and other purposes.
    """

    value: Optional[Union[bool, List[bool]]] = None
    value: Optional[Union[str, List[str]]] = None
    value: Optional[Union[float, List[float]]] = None
    value: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[str, List[str]]] = None
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    valueReference: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    valueReference: Optional[
        Union[MeasurementTypeEnumeration, List[MeasurementTypeEnumeration]]
    ] = None
    valueReference: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[Enumeration, List[Enumeration]]] = None
    valueReference: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    valueReference: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    unitCode: Optional[Union[str, List[str]]] = None
    unitCode: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    maxValue: Optional[Union[float, List[float]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    unitText: Optional[Union[str, List[str]]] = None
