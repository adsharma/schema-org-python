from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class Brand(Intangible):
    """
    A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    """

    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    slogan: Optional[Union[str, List[str]]] = None
