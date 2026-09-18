from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class MusicComposition(CreativeWork):
    """
    A musical composition.
    """

    composer: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    firstPerformance: Optional[Union[Event, List[Event]]] = None
    includedComposition: Optional[
        Union["MusicComposition", List["MusicComposition"]]
    ] = None
    iswcCode: Optional[Union[str, List[str]]] = None
    lyricist: Optional[Union[Person, List[Person]]] = None
    lyrics: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    musicArrangement: Optional[Union["MusicComposition", List["MusicComposition"]]] = (
        None
    )
    musicCompositionForm: Optional[Union[str, List[str]]] = None
    musicalKey: Optional[Union[str, List[str]]] = None
    recordedAs: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
