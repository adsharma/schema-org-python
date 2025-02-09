from typing import List, Optional, Union

from schema_models.demand import Demand
from schema_models.offer import Offer


class AggregateOffer(Offer):
    highPrice: Optional[Union[str, List[str]]] = None
    highPrice: Optional[Union[float, List[float]]] = None
    offerCount: Optional[Union[int, List[int]]] = None
    lowPrice: Optional[Union[str, List[str]]] = None
    lowPrice: Optional[Union[float, List[float]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
