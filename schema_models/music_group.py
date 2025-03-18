from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.item_list import ItemList
from schema_models.music_recording import MusicRecording
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class MusicGroup(PerformingGroup):
    """
    A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.
    """

    albums: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = None
    musicGroupMember: Optional[Union[Person, List[Person]]] = None
    track: Optional[
        Union[ItemList, List[ItemList], MusicRecording, List[MusicRecording]]
    ] = None
    album: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = None
    genre: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    tracks: Optional[Union[MusicRecording, List[MusicRecording]]] = None
