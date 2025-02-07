from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList
from schema_models.list_item import ListItem
from schema_models.rating import Rating
from schema_models.review import Review
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.web_content import WebContent


class Review(CreativeWork):
    reviewRating: Optional[Union[Rating, List[Rating]]] = None
    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
    negativeNotes: Optional[Union[WebContent, List[WebContent]]] = None
    negativeNotes: Optional[Union[ItemList, List[ItemList]]] = None
    negativeNotes: Optional[Union[ListItem, List[ListItem]]] = None
    negativeNotes: Optional[Union[Text, List[Text]]] = None
    associatedReview: Optional[Union["Review", List["Review"]]] = None
    reviewAspect: Optional[Union[Text, List[Text]]] = None
    reviewBody: Optional[Union[Text, List[Text]]] = None
    associatedClaimReview: Optional[Union["Review", List["Review"]]] = None
    associatedMediaReview: Optional[Union["Review", List["Review"]]] = None
    positiveNotes: Optional[Union[ItemList, List[ItemList]]] = None
    positiveNotes: Optional[Union[WebContent, List[WebContent]]] = None
    positiveNotes: Optional[Union[ListItem, List[ListItem]]] = None
    positiveNotes: Optional[Union[Text, List[Text]]] = None
