from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.event import Event


@dataclass
class DeliveryEvent(Event):
    """
    An event involving the delivery of an item.
    """

    accessCode: Optional[Union[str, List[str]]] = None
    availableFrom: Optional[Union[datetime, List[datetime]]] = None
    availableThrough: Optional[Union[datetime, List[datetime]]] = None
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
