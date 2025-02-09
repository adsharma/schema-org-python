from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class DatedMoneySpecification(StructuredValue):
    currency: Optional[Union[str, List[str]]] = None
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[float, List[float]]] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
