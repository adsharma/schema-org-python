from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.civic_structure import CivicStructure
from schema_models.creative_work import CreativeWork
from schema_models.dataset import Dataset
from schema_models.local_business import LocalBusiness
from schema_models.thing import Thing
from schema_models.web_content import WebContent


class SpecialAnnouncement(CreativeWork):
    webFeed: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    webFeed: Optional[Union["DataFeed", List["DataFeed"]]] = None
    governmentBenefitsInfo: Optional[
        Union["GovernmentService", List["GovernmentService"]]
    ] = None
    publicTransportClosuresInfo: Optional[Union[WebContent, List[WebContent]]] = None
    publicTransportClosuresInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    diseasePreventionInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    diseasePreventionInfo: Optional[Union[WebContent, List[WebContent]]] = None
    diseaseSpreadStatistics: Optional[Union[WebContent, List[WebContent]]] = None
    diseaseSpreadStatistics: Optional[Union[Dataset, List[Dataset]]] = None
    diseaseSpreadStatistics: Optional[Union["Observation", List["Observation"]]] = None
    diseaseSpreadStatistics: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    announcementLocation: Optional[Union[CivicStructure, List[CivicStructure]]] = None
    announcementLocation: Optional[Union[LocalBusiness, List[LocalBusiness]]] = None
    quarantineGuidelines: Optional[Union[WebContent, List[WebContent]]] = None
    quarantineGuidelines: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    newsUpdatesAndGuidelines: Optional[Union[WebContent, List[WebContent]]] = None
    newsUpdatesAndGuidelines: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    travelBans: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    travelBans: Optional[Union[WebContent, List[WebContent]]] = None
    schoolClosuresInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    schoolClosuresInfo: Optional[Union[WebContent, List[WebContent]]] = None
    datePosted: Optional[Union[datetime, List[datetime]]] = None
    datePosted: Optional[Union[date, List[date]]] = None
    gettingTestedInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    gettingTestedInfo: Optional[Union[WebContent, List[WebContent]]] = None
