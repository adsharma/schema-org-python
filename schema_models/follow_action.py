from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.interact_action import InteractAction
from schema_models.organization import Organization
from schema_models.person import Person


class FollowAction(InteractAction):
    followee: Optional[Union[Person, List[Person]]] = None
    followee: Optional[Union[Organization, List[Organization]]] = None
