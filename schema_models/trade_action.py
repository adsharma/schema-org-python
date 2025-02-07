from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.number import Number
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text


class TradeAction(Action):
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    priceSpecification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    price: Optional[Union[Text, List[Text]]] = None
    price: Optional[Union[Number, List[Number]]] = None
