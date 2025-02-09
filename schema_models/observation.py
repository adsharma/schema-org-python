from datetime import datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.place import Place
from schema_models.property import Property
from schema_models.property_value import PropertyValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.statistical_variable import StatisticalVariable
from schema_models.thing import Thing


class Observation(QuantitativeValue):
    measurementQualifier: Optional[Union[Enumeration, List[Enumeration]]] = None
    measurementMethod: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[str, List[str]]] = None
    measuredProperty: Optional[Union[Property, List[Property]]] = None
    observationDate: Optional[Union[datetime, List[datetime]]] = None
    observationAbout: Optional[Union[Place, List[Place]]] = None
    observationAbout: Optional[Union[Thing, List[Thing]]] = None
    observationPeriod: Optional[Union[str, List[str]]] = None
    measurementDenominator: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = None
    measurementTechnique: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    marginOfError: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    variableMeasured: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = None
    variableMeasured: Optional[Union[Property, List[Property]]] = None
    variableMeasured: Optional[Union[str, List[str]]] = None
    variableMeasured: Optional[Union[PropertyValue, List[PropertyValue]]] = None
