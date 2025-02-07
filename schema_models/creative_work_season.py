from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.episode import Episode
from schema_models.integer import Integer
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text
from schema_models.video_object import VideoObject


class CreativeWorkSeason(CreativeWork):
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    seasonNumber: Optional[Union[Integer, List[Integer]]] = None
    seasonNumber: Optional[Union[Text, List[Text]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    partOfSeries: Optional[Union[CreativeWorkSeries, List[CreativeWorkSeries]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    numberOfEpisodes: Optional[Union[Integer, List[Integer]]] = None
