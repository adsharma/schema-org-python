from typing import List, Optional, Union

from schema_models.media_object import MediaObject
from schema_models.text import Text


class AudioObject(MediaObject):
    embeddedTextCaption: Optional[Union[Text, List[Text]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject]]] = None
    caption: Optional[Union[Text, List[Text]]] = None
    transcript: Optional[Union[Text, List[Text]]] = None
