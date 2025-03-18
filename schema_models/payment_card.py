from typing import List, Optional, Union

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount


class PaymentCard(FinancialProduct):
    """
    A payment method using a credit, debit, store or other card to associate the payment with an account.
    """

    cashBack: Optional[Union[bool, List[bool], float, List[float]]] = None
    contactlessPayment: Optional[Union[bool, List[bool]]] = None
    floorLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    monthlyMinimumRepaymentAmount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]
    ] = None
