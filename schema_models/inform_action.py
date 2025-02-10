from typing import List, Optional, Union

from schema_models.communicate_action import CommunicateAction
from schema_models.event import Event


class InformAction(CommunicateAction):
    """
    The act of notifying someone of information pertinent to them, with no expectation of a response.
    """

    event: Optional[Union[Event, List[Event]]] = None
