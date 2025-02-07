from typing import List, Optional, Union

from schema_models.integer import Integer
from schema_models.rating import Rating
from schema_models.thing import Thing


class AggregateRating(Rating):
    reviewCount: Optional[Union[Integer, List[Integer]]] = None
    ratingCount: Optional[Union[Integer, List[Integer]]] = None
    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
