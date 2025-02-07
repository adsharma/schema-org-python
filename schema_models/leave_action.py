from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.event import Event
from schema_models.interact_action import InteractAction


class LeaveAction(InteractAction):
    event: Optional[Union[Event, List[Event]]] = None
