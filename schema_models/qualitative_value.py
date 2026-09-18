from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration
from schema_models.structured_value import StructuredValue


@dataclass
class QualitativeValue(Enumeration):
    """
    A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.
    """

    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    equal: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    greater: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    greaterOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    lesser: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    lesserOrEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    nonEqual: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
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
            "QualitativeValue",
            List["QualitativeValue"],
            "QuantitativeValue",
            List["QuantitativeValue"],
            StructuredValue,
            List[StructuredValue],
            str,
            List[str],
        ]
    ] = None
