from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.item_list import ItemList


class MusicPlaylist(CreativeWork):
    tracks: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
    numTracks: Optional[Union[Integer, List[Integer]]] = None
    track: Optional[Union[ItemList, List[ItemList]]] = None
    track: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
