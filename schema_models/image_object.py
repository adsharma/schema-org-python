from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.media_object import MediaObject


@dataclass
class ImageObject(MediaObject):
    """
    An image file.
    """

    caption: Optional[Union[MediaObject, List[MediaObject], str, List[str]]] = None
    embeddedTextCaption: Optional[Union[str, List[str]]] = None
    exifData: Optional[
        Union["PropertyValue", List["PropertyValue"], str, List[str]]
    ] = None
    representativeOfPage: Optional[Union[bool, List[bool]]] = None
