from typing import List, Optional, Union

from schema_models.media_object import MediaObject
from schema_models.music_group import MusicGroup
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class VideoObject(MediaObject):
    """
    A video file.
    """

    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    videoFrameSize: Optional[Union[str, List[str]]] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    transcript: Optional[Union[str, List[str]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[Person, List[Person], MusicGroup, List[MusicGroup]]] = None
    videoQuality: Optional[Union[str, List[str]]] = None
