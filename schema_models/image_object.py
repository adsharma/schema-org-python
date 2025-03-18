from typing import List, Optional, Union

from schema_models.media_object import MediaObject
from schema_models.property_value import PropertyValue


class ImageObject(MediaObject):
    """
    An image file.
    """

    representativeOfPage: Optional[Union[bool, List[bool]]] = None
    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    exifData: Optional[Union[str, List[str], PropertyValue, List[PropertyValue]]] = None
    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
