from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Episode(CreativeWork):
    """
    An episode of a TV, radio or game media within a series or season.
    """

    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    episodeNumber: Optional[Union[int, List[int], str, List[str]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    partOfSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    partOfSeries: Optional[Union[CreativeWorkSeries, List[CreativeWorkSeries]]] = None
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
