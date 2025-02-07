from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.loan_or_credit import LoanOrCredit
from schema_models.monetary_amount import MonetaryAmount


class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Optional[Union[Boolean, List[Boolean]]] = None
    loanMortgageMandateAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = (
        None
    )
