from typing import List, Optional, Union

from schema_models.quantitative_value_distribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """
    A statistical distribution of monetary amounts.
    """

    currency: Optional[Union[str, List[str]]] = None
