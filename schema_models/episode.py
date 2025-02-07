from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.duration import Duration
from schema_models.integer import Integer
from schema_models.music_group import MusicGroup
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text
from schema_models.video_object import VideoObject


class Episode(CreativeWork):
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    partOfSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    episodeNumber: Optional[Union[Text, List[Text]]] = None
    episodeNumber: Optional[Union[Integer, List[Integer]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    duration: Optional[Union[Duration, List[Duration]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    partOfSeries: Optional[Union[CreativeWorkSeries, List[CreativeWorkSeries]]] = None
