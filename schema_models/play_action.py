from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.audience import Audience
from schema_models.event import Event


class PlayAction(Action):
    event: Optional[Union[Event, List[Event]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
