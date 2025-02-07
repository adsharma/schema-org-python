from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.interact_action import InteractAction


class LeaveAction(InteractAction):
    event: Optional[Union[Event, List[Event]]] = None
