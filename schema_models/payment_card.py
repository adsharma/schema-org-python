from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number


class PaymentCard(FinancialProduct):
    cashBack: Optional[Union[Boolean, List[Boolean]]] = None
    cashBack: Optional[Union[Number, List[Number]]] = None
    contactlessPayment: Optional[Union[Boolean, List[Boolean]]] = None
    floorLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    monthlyMinimumRepaymentAmount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = None
    monthlyMinimumRepaymentAmount: Optional[Union[Number, List[Number]]] = None
