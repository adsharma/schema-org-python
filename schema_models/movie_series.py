from typing import List, Optional, Union

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.music_group import MusicGroup
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.video_object import VideoObject


class MovieSeries(CreativeWorkSeries):
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
