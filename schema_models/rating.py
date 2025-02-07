from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text


class Rating(Intangible):
    reviewAspect: Optional[Union[Text, List[Text]]] = None
    worstRating: Optional[Union[Number, List[Number]]] = None
    worstRating: Optional[Union[Text, List[Text]]] = None
    author: Optional[Union[Person, List[Person]]] = None
    author: Optional[Union[Organization, List[Organization]]] = None
    ratingExplanation: Optional[Union[Text, List[Text]]] = None
    ratingValue: Optional[Union[Number, List[Number]]] = None
    ratingValue: Optional[Union[Text, List[Text]]] = None
    bestRating: Optional[Union[Number, List[Number]]] = None
    bestRating: Optional[Union[Text, List[Text]]] = None
