from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.episode import Episode
from schema_models.music_group import MusicGroup
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.video_object import VideoObject


class RadioSeries(CreativeWorkSeries):
    """
    CreativeWorkSeries dedicated to radio broadcast and associated online delivery.
    """

    numberOfSeasons: Optional[Union[int, List[int]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    numberOfEpisodes: Optional[Union[int, List[int]]] = None
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    episode: Optional[Union[Episode, List[Episode]]] = None
    season: Optional[
        Union[HttpUrl, List[HttpUrl], CreativeWorkSeason, List[CreativeWorkSeason]]
    ] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
    directors: Optional[Union[Person, List[Person]]] = None
    episodes: Optional[Union[Episode, List[Episode]]] = None
    musicBy: Optional[Union[Person, List[Person], MusicGroup, List[MusicGroup]]] = None
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
