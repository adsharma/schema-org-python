from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.music_composition import MusicComposition
from schema_models.music_playlist import MusicPlaylist
from schema_models.person import Person


@dataclass
class MusicRecording(CreativeWork):
    """
    A music recording (track), usually a single song.
    """

    byArtist: Optional[
        Union["MusicGroup", List["MusicGroup"], Person, List[Person]]
    ] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    inAlbum: Optional[Union["MusicAlbum", List["MusicAlbum"]]] = None
    inPlaylist: Optional[Union[MusicPlaylist, List[MusicPlaylist]]] = None
    isrcCode: Optional[Union[str, List[str]]] = None
    recordingOf: Optional[Union[MusicComposition, List[MusicComposition]]] = None
