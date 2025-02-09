from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.media_subscription import MediaSubscription
from schema_models.organization import Organization
from schema_models.place import Place


class MediaObject(CreativeWork):
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[str, List[str]]] = None
    ineligibleRegion: Optional[Union["GeoShape", List["GeoShape"]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    uploadDate: Optional[Union[date, List[date]]] = None
    uploadDate: Optional[Union[datetime, List[datetime]]] = None
    sha256: Optional[Union[str, List[str]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    bitrate: Optional[Union[str, List[str]]] = None
    regionsAllowed: Optional[Union[Place, List[Place]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    startTime: Optional[Union[datetime, List[datetime]]] = None
    startTime: Optional[Union[time, List[time]]] = None
    encodesCreativeWork: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    width: Optional[Union["Distance", List["Distance"]]] = None
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    contentSize: Optional[Union[str, List[str]]] = None
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    encodingFormat: Optional[Union[str, List[str]]] = None
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = None
    associatedArticle: Optional[Union["NewsArticle", List["NewsArticle"]]] = None
    embedUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    contentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    endTime: Optional[Union[datetime, List[datetime]]] = None
    endTime: Optional[Union[time, List[time]]] = None
    playerType: Optional[Union[str, List[str]]] = None
    requiresSubscription: Optional[Union[bool, List[bool]]] = None
    requiresSubscription: Optional[
        Union[MediaSubscription, List[MediaSubscription]]
    ] = None
