from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class RepaymentSpecification(StructuredValue):
    """
    A structured value representing repayment.
    """

    loanPaymentAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    loanPaymentFrequency: Optional[Union[float, List[float]]] = None
    numberOfLoanPayments: Optional[Union[float, List[float]]] = None
    downPayment: Optional[
        Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]
    ] = None
    earlyPrepaymentPenalty: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
