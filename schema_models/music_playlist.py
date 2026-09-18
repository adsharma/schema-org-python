from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class MusicPlaylist(CreativeWork):
    """
    A collection of music tracks in playlist form.
    """

    numTracks: Optional[Union[int, List[int]]] = None
    track: Optional[
        Union["ItemList", List["ItemList"], "MusicRecording", List["MusicRecording"]]
    ] = None
    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
