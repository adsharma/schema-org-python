from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.quantitative_value import QuantitativeValue
from schema_models.repayment_specification import RepaymentSpecification
from schema_models.thing import Thing


@dataclass
class LoanOrCredit(FinancialProduct):
    """
    A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.
    """

    amount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]
    ] = None
    currency: Optional[Union[str, List[str]]] = None
    gracePeriod: Optional[Union[Duration, List[Duration]]] = None
    loanRepaymentForm: Optional[
        Union[RepaymentSpecification, List[RepaymentSpecification]]
    ] = None
    loanTerm: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    loanType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    recourseLoan: Optional[Union[bool, List[bool]]] = None
    renegotiableLoan: Optional[Union[bool, List[bool]]] = None
    requiredCollateral: Optional[Union[str, List[str], Thing, List[Thing]]] = None
