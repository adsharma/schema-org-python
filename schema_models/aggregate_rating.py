from typing import List, Optional, Union

from schema_models.rating import Rating
from schema_models.thing import Thing


class AggregateRating(Rating):
    """
    The average rating based on multiple ratings or reviews.
    """

    reviewCount: Optional[Union[int, List[int]]] = None
    ratingCount: Optional[Union[int, List[int]]] = None
    itemReviewed: Optional[Union[Thing, List[Thing]]] = None
