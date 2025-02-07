from typing import List, Optional, Union

from schema_models.date_time import DateTime
from schema_models.event import Event
from schema_models.text import Text


class DeliveryEvent(Event):
    availableThrough: Optional[Union[DateTime, List[DateTime]]] = None
    availableFrom: Optional[Union[DateTime, List[DateTime]]] = None
    accessCode: Optional[Union[Text, List[Text]]] = None
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = None
