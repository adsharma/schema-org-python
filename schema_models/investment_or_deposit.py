from typing import List, Optional, Union

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount


class InvestmentOrDeposit(FinancialProduct):
    """
    A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.
    """

    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[float, List[float]]] = None
