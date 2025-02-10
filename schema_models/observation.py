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
    """
    Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

    Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

    In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].

    """

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
