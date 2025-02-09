from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.media_manipulation_rating_enumeration import (
    MediaManipulationRatingEnumeration,
)
from schema_models.media_object import MediaObject
from schema_models.review import Review
from schema_models.web_page import WebPage


class MediaReview(Review):
    originalMediaContextDescription: Optional[Union[str, List[str]]] = None
    mediaAuthenticityCategory: Optional[
        Union[
            MediaManipulationRatingEnumeration, List[MediaManipulationRatingEnumeration]
        ]
    ] = None
    originalMediaLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    originalMediaLink: Optional[Union[WebPage, List[WebPage]]] = None
    originalMediaLink: Optional[Union[MediaObject, List[MediaObject]]] = None
