from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class Brand(Intangible):
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    slogan: Optional[Union[str, List[str]]] = None
