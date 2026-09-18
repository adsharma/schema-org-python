from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.rating import Rating
from schema_models.thing import Thing


@dataclass
class AggregateRating(Rating):
    """
    The overall rating, based on a collection of reviews or ratings, of the item.
    """

    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
    ratingCount: Optional[Union[int, List[int]]] = None
    reviewCount: Optional[Union[int, List[int]]] = None
