from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.quantitative_value import QuantitativeValue


class BusinessAudience(Audience):
    """
    A set of characteristics belonging to businesses, e.g. who compose an item's target audience.
    """

    yearsInOperation: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    yearlyRevenue: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfEmployees: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
