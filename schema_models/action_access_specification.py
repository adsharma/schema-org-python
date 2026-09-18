from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.place import Place
from schema_models.thing import Thing


@dataclass
class ActionAccessSpecification(Intangible):
    """
    A set of requirements that must be fulfilled in order to perform an Action.
    """

    availabilityEnds: Optional[
        Union[date, List[date], datetime, List[datetime], time, List[time]]
    ] = None
    availabilityStarts: Optional[
        Union[date, List[date], datetime, List[datetime], time, List[time]]
    ] = None
    category: Optional[
        Union[
            "CategoryCode",
            List["CategoryCode"],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            str,
            List[str],
            Thing,
            List[Thing],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    eligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = None
    ineligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    requiresSubscription: Optional[
        Union[bool, List[bool], "MediaSubscription", List["MediaSubscription"]]
    ] = None
