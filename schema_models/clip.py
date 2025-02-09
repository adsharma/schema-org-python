from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.episode import Episode
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class Clip(CreativeWork):
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"]]] = None
    partOfSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = (
        None
    )
    clipNumber: Optional[Union[str, List[str]]] = None
    clipNumber: Optional[Union[int, List[int]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    endOffset: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
    endOffset: Optional[Union[float, List[float]]] = None
    startOffset: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
    startOffset: Optional[Union[float, List[float]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    partOfEpisode: Optional[Union[Episode, List[Episode]]] = None
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
