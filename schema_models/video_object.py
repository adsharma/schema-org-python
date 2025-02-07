from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.media_object import MediaObject
from schema_models.music_group import MusicGroup
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text


class VideoObject(MediaObject):
    embeddedTextCaption: Optional[Union[Text, List[Text]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    videoFrameSize: Optional[Union[Text, List[Text]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject]]] = None
    caption: Optional[Union[Text, List[Text]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    transcript: Optional[Union[Text, List[Text]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    videoQuality: Optional[Union[Text, List[Text]]] = None
