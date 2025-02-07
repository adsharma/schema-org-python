from typing import List, Optional, Union

from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.text import Text
from schema_models.url import URL


class BankAccount(FinancialProduct):
    bankAccountType: Optional[Union[URL, List[URL]]] = None
    bankAccountType: Optional[Union[Text, List[Text]]] = None
    accountOverdraftLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    accountMinimumInflow: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
