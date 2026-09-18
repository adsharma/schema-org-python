from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.service import Service


@dataclass
class FinancialProduct(Service):
    """
    A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.
    """

    annualPercentageRate: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    feesAndCommissionsSpecification: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    interestRate: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
