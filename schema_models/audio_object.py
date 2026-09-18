from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.media_object import MediaObject


@dataclass
class AudioObject(MediaObject):
    """
    An audio file.
    """

    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    transcript: Optional[Union[str, List[str]]] = None
