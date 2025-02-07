from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.item_list import ItemList
from schema_models.music_recording import MusicRecording


class MusicPlaylist(CreativeWork):
    tracks: Optional[Union[MusicRecording, List[MusicRecording]]] = None
    numTracks: Optional[Union[Integer, List[Integer]]] = None
    track: Optional[Union[ItemList, List[ItemList]]] = None
    track: Optional[Union[MusicRecording, List[MusicRecording]]] = None
