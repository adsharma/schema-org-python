from typing import List, Optional, Union

from schema_models.how_to_item import HowToItem
from schema_models.monetary_amount import MonetaryAmount


class HowToSupply(HowToItem):
    """
    A supply consumed when performing the instructions for how to achieve a result.
    """

    estimatedCost: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    estimatedCost: Optional[Union[str, List[str]]] = None
