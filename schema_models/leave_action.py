from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.interact_action import InteractAction


class LeaveAction(InteractAction):
    """
    An agent leaves an event / group with participants/friends at a location.

    Related actions:

    * [[JoinAction]]: The antonym of LeaveAction.
    * [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.
    """

    event: Optional[Union[Event, List[Event]]] = None
