from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


class Rating(Intangible):
    reviewAspect: Optional[Union[str, List[str]]] = None
    worstRating: Optional[Union[float, List[float]]] = None
    worstRating: Optional[Union[str, List[str]]] = None
    author: Optional[Union[Person, List[Person]]] = None
    author: Optional[Union[Organization, List[Organization]]] = None
    ratingExplanation: Optional[Union[str, List[str]]] = None
    ratingValue: Optional[Union[float, List[float]]] = None
    ratingValue: Optional[Union[str, List[str]]] = None
    bestRating: Optional[Union[float, List[float]]] = None
    bestRating: Optional[Union[str, List[str]]] = None
