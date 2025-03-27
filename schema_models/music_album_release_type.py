from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MusicAlbumReleaseType(Enumeration):
    """
    The kind of release which this album is: single, EP or album.
    """
