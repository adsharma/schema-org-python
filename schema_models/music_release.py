from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.music_album import MusicAlbum
from schema_models.music_playlist import MusicPlaylist
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class MusicRelease(MusicPlaylist):
    """
    A MusicRelease is a specific release of a music album.
    """

    catalogNumber: Optional[Union[str, List[str]]] = None
    creditedTo: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    musicReleaseFormat: Optional[
        Union["MusicReleaseFormatType", List["MusicReleaseFormatType"]]
    ] = None
    recordLabel: Optional[Union[Organization, List[Organization]]] = None
    releaseOf: Optional[Union[MusicAlbum, List[MusicAlbum]]] = None
