from typing import List, Optional, Union

from schema_models.quantitative_value_distribution import QuantitativeValueDistribution
from schema_models.text import Text


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    currency: Optional[Union[Text, List[Text]]] = None
