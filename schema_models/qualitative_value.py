from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.structured_value import StructuredValue


class QualitativeValue(Enumeration):
    """
    A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.
    """

    greaterOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    greater: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    nonEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    equal: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
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
            "QualitativeValue",
            List["QualitativeValue"],
            "QuantitativeValue",
            List["QuantitativeValue"],
        ]
    ] = None
    lesser: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    lesserOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
