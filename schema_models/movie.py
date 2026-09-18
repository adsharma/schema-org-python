from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Movie(CreativeWork):
    """
    A movie.
    """

    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    subtitleLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = (
        None
    )
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
