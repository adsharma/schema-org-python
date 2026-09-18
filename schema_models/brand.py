from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.review import Review


@dataclass
class Brand(Intangible):
    """
    The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
    """

    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    review: Optional[Union[Review, List[Review]]] = None
    slogan: Optional[Union[str, List[str]]] = None
