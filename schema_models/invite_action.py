from typing import List, Optional, Union

from schema_models.communicate_action import CommunicateAction
from schema_models.event import Event


class InviteAction(CommunicateAction):
    event: Optional[Union[Event, List[Event]]] = None
