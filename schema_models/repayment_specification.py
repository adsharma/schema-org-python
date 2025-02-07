from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.structured_value import StructuredValue


class RepaymentSpecification(StructuredValue):
    loanPaymentAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    loanPaymentFrequency: Optional[Union[Number, List[Number]]] = None
    numberOfLoanPayments: Optional[Union[Number, List[Number]]] = None
    downPayment: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    downPayment: Optional[Union[Number, List[Number]]] = None
    earlyPrepaymentPenalty: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
