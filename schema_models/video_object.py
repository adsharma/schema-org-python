from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.media_object import MediaObject
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


@dataclass
class VideoObject(MediaObject):
    """
    A video file.
    """

    actor: Optional[
        Union[PerformingGroup, List[PerformingGroup], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    transcript: Optional[Union[str, List[str]]] = None
    videoFrameSize: Optional[Union[str, List[str]]] = None
    videoQuality: Optional[Union[str, List[str]]] = None
