from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.quantitative_value_distribution import QuantitativeValueDistribution
from schema_models.text import Text


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    currency: Optional[Union[Text, List[Text]]] = None
