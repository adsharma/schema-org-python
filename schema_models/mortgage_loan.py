from typing import List, Optional, Union

from schema_models.loan_or_credit import LoanOrCredit
from schema_models.monetary_amount import MonetaryAmount


class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Optional[Union[bool, List[bool]]] = None
    loanMortgageMandateAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = (
        None
    )
