from typing import List, Optional, Union

from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.episode import Episode
from schema_models.integer import Integer
from schema_models.music_group import MusicGroup
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.url import URL
from schema_models.video_object import VideoObject


class RadioSeries(CreativeWorkSeries):
    numberOfSeasons: Optional[Union[Integer, List[Integer]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    numberOfEpisodes: Optional[Union[Integer, List[Integer]]] = None
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    season: Optional[Union[URL, List[URL]]] = None
    season: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
