from typing import List, Optional, Union

from schema_models.music_album_production_type import MusicAlbumProductionType
from schema_models.music_album_release_type import MusicAlbumReleaseType
from schema_models.music_group import MusicGroup
from schema_models.music_playlist import MusicPlaylist
from schema_models.music_release import MusicRelease
from schema_models.person import Person


class MusicAlbum(MusicPlaylist):
    byArtist: Optional[Union[Person, List[Person]]] = None
    byArtist: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    albumRelease: Optional[Union[MusicRelease, List[MusicRelease]]] = None
    albumProductionType: Optional[
        Union[MusicAlbumProductionType, List[MusicAlbumProductionType]]
    ] = None
    albumReleaseType: Optional[
        Union[MusicAlbumReleaseType, List[MusicAlbumReleaseType]]
    ] = None
