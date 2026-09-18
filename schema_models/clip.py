from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


@dataclass
class Clip(CreativeWork):
    """
    A short TV or radio program or a segment/part of a program.
    """

    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    clipNumber: Optional[Union[int, List[int], str, List[str]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    endOffset: Optional[
        Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]
    ] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    partOfEpisode: Optional[Union["Episode", List["Episode"]]] = None
    partOfSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = (
        None
    )
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = (
        None
    )
    startOffset: Optional[
        Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]
    ] = None
