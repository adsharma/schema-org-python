from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList


class MusicPlaylist(CreativeWork):
    """
    A collection of music tracks in playlist form.
    """

    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
    numTracks: Optional[Union[int, List[int]]] = None
    track: Optional[
        Union[ItemList, List[ItemList], "MusicRecording", List["MusicRecording"]]
    ] = None
