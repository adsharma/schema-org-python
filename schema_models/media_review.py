from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.media_manipulation_rating_enumeration import (
    MediaManipulationRatingEnumeration,
)
from schema_models.media_object import MediaObject
from schema_models.review import Review
from schema_models.web_page import WebPage


class MediaReview(Review):
    """
    A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.
        For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is
        a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working
        to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.
    """

    originalMediaContextDescription: Optional[Union[str, List[str]]] = None
    mediaAuthenticityCategory: Optional[
        Union[
            MediaManipulationRatingEnumeration, List[MediaManipulationRatingEnumeration]
        ]
    ] = None
    originalMediaLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    originalMediaLink: Optional[Union[WebPage, List[WebPage]]] = None
    originalMediaLink: Optional[Union[MediaObject, List[MediaObject]]] = None
