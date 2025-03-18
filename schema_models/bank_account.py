from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount


class BankAccount(FinancialProduct):
    """
    A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.
    """

    bankAccountType: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = None
    accountOverdraftLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    accountMinimumInflow: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
