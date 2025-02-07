from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.duration import Duration
from schema_models.music_album import MusicAlbum
from schema_models.music_playlist import MusicPlaylist
from schema_models.music_release_format_type import MusicReleaseFormatType
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text


class MusicRelease(MusicPlaylist):
    duration: Optional[Union[Duration, List[Duration]]] = None
    releaseOf: Optional[Union[MusicAlbum, List[MusicAlbum]]] = None
    catalogNumber: Optional[Union[Text, List[Text]]] = None
    creditedTo: Optional[Union[Person, List[Person]]] = None
    creditedTo: Optional[Union[Organization, List[Organization]]] = None
    recordLabel: Optional[Union[Organization, List[Organization]]] = None
    musicReleaseFormat: Optional[
        Union[MusicReleaseFormatType, List[MusicReleaseFormatType]]
    ] = None
