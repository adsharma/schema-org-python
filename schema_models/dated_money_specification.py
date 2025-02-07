from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class DatedMoneySpecification(StructuredValue):
    currency: Optional[Union[Text, List[Text]]] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[Number, List[Number]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
