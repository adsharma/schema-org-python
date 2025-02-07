from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.how_to_item import HowToItem
from schema_models.monetary_amount import MonetaryAmount
from schema_models.text import Text


class HowToSupply(HowToItem):
    estimatedCost: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    estimatedCost: Optional[Union[Text, List[Text]]] = None
