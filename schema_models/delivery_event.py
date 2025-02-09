from datetime import datetime
from typing import List, Optional, Union

from schema_models.event import Event


class DeliveryEvent(Event):
    availableThrough: Optional[Union[datetime, List[datetime]]] = None
    availableFrom: Optional[Union[datetime, List[datetime]]] = None
    accessCode: Optional[Union[str, List[str]]] = None
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
