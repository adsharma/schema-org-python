from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.category_code import CategoryCode
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.geo_shape import GeoShape
from schema_models.intangible import Intangible
from schema_models.media_subscription import MediaSubscription
from schema_models.offer import Offer
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.place import Place
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.time import Time
from schema_models.url import URL


class ActionAccessSpecification(Intangible):
    requiresSubscription: Optional[Union[Boolean, List[Boolean]]] = None
    requiresSubscription: Optional[
        Union[MediaSubscription, List[MediaSubscription]]
    ] = None
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = None
    availabilityEnds: Optional[Union[DateTime, List[DateTime]]] = None
    availabilityEnds: Optional[Union[Time, List[Time]]] = None
    availabilityEnds: Optional[Union[Date, List[Date]]] = None
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[Text, List[Text]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    availabilityStarts: Optional[Union[Date, List[Date]]] = None
    availabilityStarts: Optional[Union[Time, List[Time]]] = None
    availabilityStarts: Optional[Union[DateTime, List[DateTime]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    eligibleRegion: Optional[Union[Text, List[Text]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
