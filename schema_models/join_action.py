from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.interact_action import InteractAction


class JoinAction(InteractAction):
    """
    An agent joins an event/group with participants/friends at a location.

    Related actions:

    * [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.
    * [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.
    * [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.
    """

    event: Optional[Union[Event, List[Event]]] = None
