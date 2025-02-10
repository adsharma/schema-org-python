from typing import List, Optional, Union

from schema_models.delivery_method import DeliveryMethod
from schema_models.find_action import FindAction


class TrackAction(FindAction):
    """
    An agent tracks an object for updates.

    Related actions:

    * [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.
    * [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.
    """

    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
