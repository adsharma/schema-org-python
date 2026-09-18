from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.enumeration import Enumeration
from schema_models.intangible import Intangible
from schema_models.place import Place
from schema_models.thing import Thing


@dataclass
class Observation(Intangible):
    """
    Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

    Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

    In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].

    """

    marginOfError: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    measuredProperty: Optional[Union["Property", List["Property"]]] = None
    measurementDenominator: Optional[
        Union["StatisticalVariable", List["StatisticalVariable"]]
    ] = None
    measurementMethod: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    measurementQualifier: Optional[Union[Enumeration, List[Enumeration]]] = None
    measurementTechnique: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    observationAbout: Optional[Union[Place, List[Place], Thing, List[Thing]]] = None
    observationDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    observationPeriod: Optional[Union[str, List[str]]] = None
    variableMeasured: Optional[
        Union[
            "Property",
            List["Property"],
            "PropertyValue",
            List["PropertyValue"],
            "StatisticalVariable",
            List["StatisticalVariable"],
            str,
            List[str],
        ]
    ] = None
