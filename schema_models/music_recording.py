from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.music_album import MusicAlbum
from schema_models.music_composition import MusicComposition
from schema_models.music_group import MusicGroup
from schema_models.music_playlist import MusicPlaylist
from schema_models.person import Person
from schema_models.text import Text


class MusicRecording(CreativeWork):
    byArtist: Optional[Union[Person, List[Person]]] = None
    byArtist: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    inPlaylist: Optional[Union[MusicPlaylist, List[MusicPlaylist]]] = None
    duration: Optional[Union[Duration, List[Duration]]] = None
    recordingOf: Optional[Union[MusicComposition, List[MusicComposition]]] = None
    isrcCode: Optional[Union[Text, List[Text]]] = None
    inAlbum: Optional[Union[MusicAlbum, List[MusicAlbum]]] = None
