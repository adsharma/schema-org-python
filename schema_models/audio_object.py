from typing import List, Optional, Union

from schema_models.media_object import MediaObject


class AudioObject(MediaObject):
    """
    An audio file.
    """

    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
    transcript: Optional[Union[str, List[str]]] = None
