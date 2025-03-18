from typing import List, Optional, Union

from schema_models.demand import Demand
from schema_models.offer import Offer


class AggregateOffer(Offer):
    """
    When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.

    Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.
    """

    highPrice: Optional[Union[str, List[str], float, List[float]]] = None
    offerCount: Optional[Union[int, List[int]]] = None
    lowPrice: Optional[Union[str, List[str], float, List[float]]] = None
    offers: Optional[Union[Offer, List[Offer], Demand, List[Demand]]] = None
