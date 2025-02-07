from typing import List, Optional, Union

from schema_models.delivery_method import DeliveryMethod
from schema_models.find_action import FindAction


class TrackAction(FindAction):
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
