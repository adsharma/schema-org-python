from typing import List, Optional, Union

from schema_models.__class import _Class
from schema_models.constraint_node import ConstraintNode
from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.property import Property
from schema_models.text import Text
from schema_models.url import URL


class StatisticalVariable(ConstraintNode):
    measurementDenominator: Optional[
        Union["StatisticalVariable", List["StatisticalVariable"]]
    ] = None
    populationType: Optional[Union[_Class, List[_Class]]] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementQualifier: Optional[Union[Enumeration, List[Enumeration]]] = None
    measuredProperty: Optional[Union[Property, List[Property]]] = None
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    statType: Optional[Union[Property, List[Property]]] = None
    statType: Optional[Union[Text, List[Text]]] = None
    statType: Optional[Union[URL, List[URL]]] = None
