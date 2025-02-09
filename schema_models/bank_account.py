from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount


class BankAccount(FinancialProduct):
    bankAccountType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    bankAccountType: Optional[Union[str, List[str]]] = None
    accountOverdraftLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    accountMinimumInflow: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
