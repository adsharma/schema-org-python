from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


class ComicStory(CreativeWork):
    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
