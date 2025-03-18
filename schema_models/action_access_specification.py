from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.media_subscription import MediaSubscription
from schema_models.offer import Offer
from schema_models.place import Place
from schema_models.thing import Thing


class ActionAccessSpecification(Intangible):
    """
    A set of requirements that must be fulfilled in order to perform an Action.
    """

    requiresSubscription: Optional[
        Union[bool, List[bool], MediaSubscription, List[MediaSubscription]]
    ] = None
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = None
    availabilityEnds: Optional[
        Union[datetime, List[datetime], time, List[time], date, List[date]]
    ] = None
    ineligibleRegion: Optional[
        Union[Place, List[Place], str, List[str], "GeoShape", List["GeoShape"]]
    ] = None
    availabilityStarts: Optional[
        Union[date, List[date], time, List[time], datetime, List[datetime]]
    ] = None
    category: Optional[
        Union[
            Thing,
            List[Thing],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            "CategoryCode",
            List["CategoryCode"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    eligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], str, List[str], Place, List[Place]]
    ] = None
