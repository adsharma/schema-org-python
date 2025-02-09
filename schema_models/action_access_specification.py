from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.media_subscription import MediaSubscription
from schema_models.offer import Offer
from schema_models.place import Place
from schema_models.thing import Thing


class ActionAccessSpecification(Intangible):
    requiresSubscription: Optional[Union[bool, List[bool]]] = None
    requiresSubscription: Optional[
        Union[MediaSubscription, List[MediaSubscription]]
    ] = None
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = None
    availabilityEnds: Optional[Union[datetime, List[datetime]]] = None
    availabilityEnds: Optional[Union[time, List[time]]] = None
    availabilityEnds: Optional[Union[date, List[date]]] = None
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[str, List[str]]] = None
    ineligibleRegion: Optional[Union["GeoShape", List["GeoShape"]]] = None
    availabilityStarts: Optional[Union[date, List[date]]] = None
    availabilityStarts: Optional[Union[time, List[time]]] = None
    availabilityStarts: Optional[Union[datetime, List[datetime]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    eligibleRegion: Optional[Union["GeoShape", List["GeoShape"]]] = None
    eligibleRegion: Optional[Union[str, List[str]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
