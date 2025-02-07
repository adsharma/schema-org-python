from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL


class Movie(CreativeWork):
    productionCompany: Optional[Union[Organization, List[Organization]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    titleEIDR: Optional[Union[Text, List[Text]]] = None
    titleEIDR: Optional[Union[URL, List[URL]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    subtitleLanguage: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
