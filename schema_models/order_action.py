from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.delivery_method import DeliveryMethod
from schema_models.trade_action import TradeAction


class OrderAction(TradeAction):
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
