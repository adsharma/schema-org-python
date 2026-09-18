from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.claim import Claim
from schema_models.creative_work import CreativeWork
from schema_models.distance import Distance
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.place import Place


@dataclass
class MediaObject(CreativeWork):
    """
    A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).
    """

    associatedArticle: Optional[Union["NewsArticle", List["NewsArticle"]]] = None
    bitrate: Optional[Union[str, List[str]]] = None
    contentSize: Optional[Union[str, List[str]]] = None
    contentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    embedUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    encodesCreativeWork: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    encodingFormat: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    height: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    ineligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    interpretedAsClaim: Optional[Union[Claim, List[Claim]]] = None
    playerType: Optional[Union[str, List[str]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    regionsAllowed: Optional[Union[Place, List[Place]]] = None
    requiresSubscription: Optional[
        Union[bool, List[bool], "MediaSubscription", List["MediaSubscription"]]
    ] = None
    sha256: Optional[Union[str, List[str]]] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    uploadDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    width: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
