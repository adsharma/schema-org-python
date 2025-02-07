from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.media_object import MediaObject
from schema_models.property_value import PropertyValue
from schema_models.text import Text


class ImageObject(MediaObject):
    representativeOfPage: Optional[Union[Boolean, List[Boolean]]] = None
    embeddedTextCaption: Optional[Union[Text, List[Text]]] = None
    exifData: Optional[Union[Text, List[Text]]] = None
    exifData: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject]]] = None
    caption: Optional[Union[Text, List[Text]]] = None
