from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class Movie(CreativeWork):
    """
    A movie.
    """

    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[Person, List[Person], "MusicGroup", List["MusicGroup"]]] = (
        None
    )
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    subtitleLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
