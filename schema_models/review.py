from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList
from schema_models.list_item import ListItem
from schema_models.rating import Rating
from schema_models.thing import Thing
from schema_models.web_content import WebContent


class Review(CreativeWork):
    """
    A review of an item - for example, of a restaurant, movie, or store.
    """

    reviewRating: Optional[Union[Rating, List[Rating]]] = None
    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
    negativeNotes: Optional[
        Union[
            WebContent,
            List[WebContent],
            ItemList,
            List[ItemList],
            ListItem,
            List[ListItem],
            str,
            List[str],
        ]
    ] = None
    associatedReview: Optional[Union["Review", List["Review"]]] = None
    reviewAspect: Optional[Union[str, List[str]]] = None
    reviewBody: Optional[Union[str, List[str]]] = None
    associatedClaimReview: Optional[Union["Review", List["Review"]]] = None
    associatedMediaReview: Optional[Union["Review", List["Review"]]] = None
    positiveNotes: Optional[
        Union[
            ItemList,
            List[ItemList],
            WebContent,
            List[WebContent],
            ListItem,
            List[ListItem],
            str,
            List[str],
        ]
    ] = None
