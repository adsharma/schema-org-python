from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.media_subscription import MediaSubscription
from schema_models.organization import Organization
from schema_models.place import Place


class MediaObject(CreativeWork):
    """
    A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).
    """

    ineligibleRegion: Optional[
        Union[Place, List[Place], str, List[str], "GeoShape", List["GeoShape"]]
    ] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    uploadDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    sha256: Optional[Union[str, List[str]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    bitrate: Optional[Union[str, List[str]]] = None
    regionsAllowed: Optional[Union[Place, List[Place]]] = None
    height: Optional[
        Union[
            "Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]
        ]
    ] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    encodesCreativeWork: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    width: Optional[
        Union[
            "Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]
        ]
    ] = None
    contentSize: Optional[Union[str, List[str]]] = None
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = None
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = None
    associatedArticle: Optional[Union["NewsArticle", List["NewsArticle"]]] = None
    embedUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    contentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    playerType: Optional[Union[str, List[str]]] = None
    requiresSubscription: Optional[
        Union[bool, List[bool], MediaSubscription, List[MediaSubscription]]
    ] = None
