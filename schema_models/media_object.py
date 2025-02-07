from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.claim import Claim
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.distance import Distance
from schema_models.duration import Duration
from schema_models.geo_shape import GeoShape
from schema_models.media_subscription import MediaSubscription
from schema_models.news_article import NewsArticle
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.time import Time
from schema_models.url import URL


class MediaObject(CreativeWork):
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[Text, List[Text]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    uploadDate: Optional[Union[Date, List[Date]]] = None
    uploadDate: Optional[Union[DateTime, List[DateTime]]] = None
    sha256: Optional[Union[Text, List[Text]]] = None
    duration: Optional[Union[Duration, List[Duration]]] = None
    bitrate: Optional[Union[Text, List[Text]]] = None
    regionsAllowed: Optional[Union[Place, List[Place]]] = None
    height: Optional[Union[Distance, List[Distance]]] = None
    height: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    startTime: Optional[Union[DateTime, List[DateTime]]] = None
    startTime: Optional[Union[Time, List[Time]]] = None
    encodesCreativeWork: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    width: Optional[Union[Distance, List[Distance]]] = None
    width: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    contentSize: Optional[Union[Text, List[Text]]] = None
    encodingFormat: Optional[Union[URL, List[URL]]] = None
    encodingFormat: Optional[Union[Text, List[Text]]] = None
    interpretedAsClaim: Optional[Union[Claim, List[Claim]]] = None
    associatedArticle: Optional[Union[NewsArticle, List[NewsArticle]]] = None
    embedUrl: Optional[Union[URL, List[URL]]] = None
    contentUrl: Optional[Union[URL, List[URL]]] = None
    endTime: Optional[Union[DateTime, List[DateTime]]] = None
    endTime: Optional[Union[Time, List[Time]]] = None
    playerType: Optional[Union[Text, List[Text]]] = None
    requiresSubscription: Optional[Union[Boolean, List[Boolean]]] = None
    requiresSubscription: Optional[
        Union[MediaSubscription, List[MediaSubscription]]
    ] = None
