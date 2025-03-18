from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.quantitative_value import QuantitativeValue
from schema_models.service import Service


class FinancialProduct(Service):
    """
    A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.
    """

    feesAndCommissionsSpecification: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    annualPercentageRate: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
    interestRate: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
