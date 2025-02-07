from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.duration import Duration
from schema_models.financial_product import FinancialProduct
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.repayment_specification import RepaymentSpecification
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class LoanOrCredit(FinancialProduct):
    loanTerm: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    requiredCollateral: Optional[Union[Thing, List[Thing]]] = None
    requiredCollateral: Optional[Union[Text, List[Text]]] = None
    loanType: Optional[Union[Text, List[Text]]] = None
    loanType: Optional[Union[URL, List[URL]]] = None
    recourseLoan: Optional[Union[Boolean, List[Boolean]]] = None
    loanRepaymentForm: Optional[
        Union[RepaymentSpecification, List[RepaymentSpecification]]
    ] = None
    gracePeriod: Optional[Union[Duration, List[Duration]]] = None
    currency: Optional[Union[Text, List[Text]]] = None
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[Number, List[Number]]] = None
    renegotiableLoan: Optional[Union[Boolean, List[Boolean]]] = None
