from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience


@dataclass
class BusinessAudience(Audience):
    """
    A set of characteristics belonging to businesses, e.g. who compose an item's target audience.
    """

    numberOfEmployees: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    yearlyRevenue: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    yearsInOperation: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
