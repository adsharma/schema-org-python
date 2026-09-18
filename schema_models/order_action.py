from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.trade_action import TradeAction


@dataclass
class OrderAction(TradeAction):
    """
    An agent orders an object/product/service to be delivered/sent.
    """

    deliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
