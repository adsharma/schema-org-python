from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.music_recording import MusicRecording
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text


class MusicComposition(CreativeWork):
    recordedAs: Optional[Union[MusicRecording, List[MusicRecording]]] = None
    musicCompositionForm: Optional[Union[Text, List[Text]]] = None
    includedComposition: Optional[
        Union["MusicComposition", List["MusicComposition"]]
    ] = None
    lyricist: Optional[Union[Person, List[Person]]] = None
    musicArrangement: Optional[Union["MusicComposition", List["MusicComposition"]]] = (
        None
    )
    musicalKey: Optional[Union[Text, List[Text]]] = None
    composer: Optional[Union[Person, List[Person]]] = None
    composer: Optional[Union[Organization, List[Organization]]] = None
    iswcCode: Optional[Union[Text, List[Text]]] = None
    lyrics: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    firstPerformance: Optional[Union[Event, List[Event]]] = None
