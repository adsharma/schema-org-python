from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.communicate_action import CommunicateAction
from schema_models.event import Event


class InviteAction(CommunicateAction):
    event: Optional[Union[Event, List[Event]]] = None
