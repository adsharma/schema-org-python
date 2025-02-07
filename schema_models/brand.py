from typing import List, Optional, Union

from schema_models.aggregate_rating import AggregateRating
from schema_models.image_object import ImageObject
from schema_models.intangible import Intangible
from schema_models.review import Review
from schema_models.text import Text
from schema_models.url import URL


class Brand(Intangible):
    aggregateRating: Optional[Union[AggregateRating, List[AggregateRating]]] = None
    review: Optional[Union[Review, List[Review]]] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union[ImageObject, List[ImageObject]]] = None
    slogan: Optional[Union[Text, List[Text]]] = None
