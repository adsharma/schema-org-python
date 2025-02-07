from typing import List, Optional, Union

from schema_models.delivery_method import DeliveryMethod
from schema_models.trade_action import TradeAction


class OrderAction(TradeAction):
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
