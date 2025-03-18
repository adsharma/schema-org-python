from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.episode import Episode
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class Clip(CreativeWork):
    """
    A short TV or radio program or a segment/part of a program.
    """

    musicBy: Optional[Union[Person, List[Person], "MusicGroup", List["MusicGroup"]]] = (
        None
    )
    partOfSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = (
        None
    )
    clipNumber: Optional[Union[str, List[str], int, List[int]]] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    endOffset: Optional[
        Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]
    ] = None
    startOffset: Optional[
        Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]
    ] = None
    directors: Optional[Union[Person, List[Person]]] = None
    partOfEpisode: Optional[Union[Episode, List[Episode]]] = None
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
