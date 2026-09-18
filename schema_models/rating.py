from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Rating(Intangible):
    """
    A rating is an evaluation on a numeric scale, such as 1 to 5 stars.
    """

    author: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    bestRating: Optional[Union[float, List[float], str, List[str]]] = None
    ratingExplanation: Optional[Union[str, List[str]]] = None
    ratingValue: Optional[Union[float, List[float], str, List[str]]] = None
    reviewAspect: Optional[
        Union["StructuredValue", List["StructuredValue"], str, List[str]]
    ] = None
    worstRating: Optional[Union[float, List[float], str, List[str]]] = None
