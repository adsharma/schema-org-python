from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.thing import Thing


@dataclass
class Review(CreativeWork):
    """
    A review of the item.
    """

    associatedClaimReview: Optional[Union["Review", List["Review"]]] = None
    associatedMediaReview: Optional[Union["Review", List["Review"]]] = None
    associatedReview: Optional[Union["Review", List["Review"]]] = None
    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
    negativeNotes: Optional[
        Union[
            "ItemList",
            List["ItemList"],
            "ListItem",
            List["ListItem"],
            str,
            List[str],
            "WebContent",
            List["WebContent"],
        ]
    ] = None
    positiveNotes: Optional[
        Union[
            "ItemList",
            List["ItemList"],
            "ListItem",
            List["ListItem"],
            str,
            List[str],
            "WebContent",
            List["WebContent"],
        ]
    ] = None
    reviewAspect: Optional[
        Union["StructuredValue", List["StructuredValue"], str, List[str]]
    ] = None
    reviewBody: Optional[Union[str, List[str]]] = None
    reviewRating: Optional[Union["Rating", List["Rating"]]] = None
