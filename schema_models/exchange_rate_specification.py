from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


@dataclass
class ExchangeRateSpecification(StructuredValue):
    """
    A structured value representing exchange rate.
    """

    currency: Optional[Union[str, List[str]]] = None
    currentExchangeRate: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    exchangeRateSpread: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
