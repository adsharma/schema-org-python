from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.music_playlist import MusicPlaylist
from schema_models.person import Person


@dataclass
class MusicAlbum(MusicPlaylist):
    """
    A collection of music tracks.
    """

    albumProductionType: Optional[
        Union["MusicAlbumProductionType", List["MusicAlbumProductionType"]]
    ] = None
    albumRelease: Optional[Union["MusicRelease", List["MusicRelease"]]] = None
    albumReleaseType: Optional[
        Union["MusicAlbumReleaseType", List["MusicAlbumReleaseType"]]
    ] = None
    byArtist: Optional[
        Union["MusicGroup", List["MusicGroup"], Person, List[Person]]
    ] = None
