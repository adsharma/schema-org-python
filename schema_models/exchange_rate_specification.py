from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class ExchangeRateSpecification(StructuredValue):
    """
    A structured value representing exchange rate.
    """

    currentExchangeRate: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    currency: Optional[Union[str, List[str]]] = None
    exchangeRateSpread: Optional[
        Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]
    ] = None
