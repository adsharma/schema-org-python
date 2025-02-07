from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.place import Place
from schema_models.property import Property
from schema_models.property_value import PropertyValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.statistical_variable import StatisticalVariable
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Observation(QuantitativeValue):
    measurementQualifier: Optional[Union[Enumeration, List[Enumeration]]] = None
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    measuredProperty: Optional[Union[Property, List[Property]]] = None
    observationDate: Optional[Union[DateTime, List[DateTime]]] = None
    observationAbout: Optional[Union[Place, List[Place]]] = None
    observationAbout: Optional[Union[Thing, List[Thing]]] = None
    observationPeriod: Optional[Union[Text, List[Text]]] = None
    measurementDenominator: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    marginOfError: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    variableMeasured: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = None
    variableMeasured: Optional[Union[Property, List[Property]]] = None
    variableMeasured: Optional[Union[Text, List[Text]]] = None
    variableMeasured: Optional[Union[PropertyValue, List[PropertyValue]]] = None
