from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.quantitative_value import QuantitativeValue
from schema_models.web_page import WebPage


class RealEstateListing(WebPage):
    """
    A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).
      The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]].

    """

    datePosted: Optional[Union[datetime, List[datetime]]] = None
    datePosted: Optional[Union[date, List[date]]] = None
    leaseLength: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    leaseLength: Optional[Union[Duration, List[Duration]]] = None
