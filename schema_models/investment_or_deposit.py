from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number


class InvestmentOrDeposit(FinancialProduct):
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[Number, List[Number]]] = None
