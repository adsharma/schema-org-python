from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


class Rating(Intangible):
    """
    A rating is an evaluation on a numeric scale, such as 1 to 5 stars.
    """

    reviewAspect: Optional[Union[str, List[str]]] = None
    worstRating: Optional[Union[float, List[float], str, List[str]]] = None
    author: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    ratingExplanation: Optional[Union[str, List[str]]] = None
    ratingValue: Optional[Union[float, List[float], str, List[str]]] = None
    bestRating: Optional[Union[float, List[float], str, List[str]]] = None
