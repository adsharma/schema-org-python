from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.quantitative_value import QuantitativeValue
from schema_models.service import Service


class FinancialProduct(Service):
    feesAndCommissionsSpecification: Optional[Union[str, List[str]]] = None
    feesAndCommissionsSpecification: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    annualPercentageRate: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    annualPercentageRate: Optional[Union[float, List[float]]] = None
    interestRate: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    interestRate: Optional[Union[float, List[float]]] = None
