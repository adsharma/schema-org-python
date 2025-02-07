from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.unit_price_specification import UnitPriceSpecification


class ExchangeRateSpecification(StructuredValue):
    currentExchangeRate: Optional[
        Union[UnitPriceSpecification, List[UnitPriceSpecification]]
    ] = None
    currency: Optional[Union[Text, List[Text]]] = None
    exchangeRateSpread: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    exchangeRateSpread: Optional[Union[Number, List[Number]]] = None
