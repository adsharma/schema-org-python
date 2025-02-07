from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.demand import Demand
from schema_models.integer import Integer
from schema_models.number import Number
from schema_models.offer import Offer
from schema_models.text import Text


class AggregateOffer(Offer):
    highPrice: Optional[Union[Text, List[Text]]] = None
    highPrice: Optional[Union[Number, List[Number]]] = None
    offerCount: Optional[Union[Integer, List[Integer]]] = None
    lowPrice: Optional[Union[Text, List[Text]]] = None
    lowPrice: Optional[Union[Number, List[Number]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
