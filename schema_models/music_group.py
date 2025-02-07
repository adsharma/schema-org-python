from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.item_list import ItemList
from schema_models.music_album import MusicAlbum
from schema_models.music_recording import MusicRecording
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL


class MusicGroup(PerformingGroup):
    albums: Optional[Union[MusicAlbum, List[MusicAlbum]]] = None
    musicGroupMember: Optional[Union[Person, List[Person]]] = None
    track: Optional[Union[ItemList, List[ItemList]]] = None
    track: Optional[Union[MusicRecording, List[MusicRecording]]] = None
    album: Optional[Union[MusicAlbum, List[MusicAlbum]]] = None
    genre: Optional[Union[Text, List[Text]]] = None
    genre: Optional[Union[URL, List[URL]]] = None
    tracks: Optional[Union[MusicRecording, List[MusicRecording]]] = None
