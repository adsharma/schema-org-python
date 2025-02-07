from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.achieve_action import AchieveAction
from schema_models.person import Person


class WinAction(AchieveAction):
    loser: Optional[Union[Person, List[Person]]] = None
