from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


@dataclass
class MovieSeries(CreativeWorkSeries):
    """
    A series of movies. Included movies can be indicated with the hasPart property.
    """

    actor: Optional[
        Union[PerformingGroup, List[PerformingGroup], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
