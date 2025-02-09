from typing import List, Optional, Union

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount


class PaymentCard(FinancialProduct):
    cashBack: Optional[Union[bool, List[bool]]] = None
    cashBack: Optional[Union[float, List[float]]] = None
    contactlessPayment: Optional[Union[bool, List[bool]]] = None
    floorLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    monthlyMinimumRepaymentAmount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = None
    monthlyMinimumRepaymentAmount: Optional[Union[float, List[float]]] = None
