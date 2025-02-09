from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.quantitative_value import QuantitativeValue
from schema_models.repayment_specification import RepaymentSpecification
from schema_models.thing import Thing


class LoanOrCredit(FinancialProduct):
    loanTerm: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    requiredCollateral: Optional[Union[Thing, List[Thing]]] = None
    requiredCollateral: Optional[Union[str, List[str]]] = None
    loanType: Optional[Union[str, List[str]]] = None
    loanType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    recourseLoan: Optional[Union[bool, List[bool]]] = None
    loanRepaymentForm: Optional[
        Union[RepaymentSpecification, List[RepaymentSpecification]]
    ] = None
    gracePeriod: Optional[Union[Duration, List[Duration]]] = None
    currency: Optional[Union[str, List[str]]] = None
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[float, List[float]]] = None
    renegotiableLoan: Optional[Union[bool, List[bool]]] = None
