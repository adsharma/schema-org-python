from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.property_value import PropertyValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class QualitativeValue(Enumeration):
    greaterOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    greater: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    nonEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    equal: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    valueReference: Optional[Union[Text, List[Text]]] = None
    valueReference: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    valueReference: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    valueReference: Optional[
        Union[MeasurementTypeEnumeration, List[MeasurementTypeEnumeration]]
    ] = None
    valueReference: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    valueReference: Optional[Union[Enumeration, List[Enumeration]]] = None
    valueReference: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    valueReference: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    lesser: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    lesserOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
