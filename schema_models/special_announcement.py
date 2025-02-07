from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.category_code import CategoryCode
from schema_models.civic_structure import CivicStructure
from schema_models.creative_work import CreativeWork
from schema_models.data_feed import DataFeed
from schema_models.dataset import Dataset
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.government_service import GovernmentService
from schema_models.local_business import LocalBusiness
from schema_models.observation import Observation
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL
from schema_models.web_content import WebContent


class SpecialAnnouncement(CreativeWork):
    webFeed: Optional[Union[URL, List[URL]]] = None
    webFeed: Optional[Union[DataFeed, List[DataFeed]]] = None
    governmentBenefitsInfo: Optional[
        Union[GovernmentService, List[GovernmentService]]
    ] = None
    publicTransportClosuresInfo: Optional[Union[WebContent, List[WebContent]]] = None
    publicTransportClosuresInfo: Optional[Union[URL, List[URL]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    diseasePreventionInfo: Optional[Union[URL, List[URL]]] = None
    diseasePreventionInfo: Optional[Union[WebContent, List[WebContent]]] = None
    diseaseSpreadStatistics: Optional[Union[WebContent, List[WebContent]]] = None
    diseaseSpreadStatistics: Optional[Union[Dataset, List[Dataset]]] = None
    diseaseSpreadStatistics: Optional[Union[Observation, List[Observation]]] = None
    diseaseSpreadStatistics: Optional[Union[URL, List[URL]]] = None
    announcementLocation: Optional[Union[CivicStructure, List[CivicStructure]]] = None
    announcementLocation: Optional[Union[LocalBusiness, List[LocalBusiness]]] = None
    quarantineGuidelines: Optional[Union[WebContent, List[WebContent]]] = None
    quarantineGuidelines: Optional[Union[URL, List[URL]]] = None
    newsUpdatesAndGuidelines: Optional[Union[WebContent, List[WebContent]]] = None
    newsUpdatesAndGuidelines: Optional[Union[URL, List[URL]]] = None
    travelBans: Optional[Union[URL, List[URL]]] = None
    travelBans: Optional[Union[WebContent, List[WebContent]]] = None
    schoolClosuresInfo: Optional[Union[URL, List[URL]]] = None
    schoolClosuresInfo: Optional[Union[WebContent, List[WebContent]]] = None
    datePosted: Optional[Union[DateTime, List[DateTime]]] = None
    datePosted: Optional[Union[Date, List[Date]]] = None
    gettingTestedInfo: Optional[Union[URL, List[URL]]] = None
    gettingTestedInfo: Optional[Union[WebContent, List[WebContent]]] = None
