from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MusicAlbumProductionType(Enumeration):
    """
    Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
