from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.music_composition import MusicComposition
from schema_models.music_playlist import MusicPlaylist
from schema_models.person import Person


class MusicRecording(CreativeWork):
    """
    A music recording (track), usually a single song.
    """

    byArtist: Optional[
        Union[Person, List[Person], "MusicGroup", List["MusicGroup"]]
    ] = None
    inPlaylist: Optional[Union[MusicPlaylist, List[MusicPlaylist]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    recordingOf: Optional[Union[MusicComposition, List[MusicComposition]]] = None
    isrcCode: Optional[Union[str, List[str]]] = None
    inAlbum: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = None
