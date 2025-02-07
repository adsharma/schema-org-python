from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.choose_action import ChooseAction
from schema_models.person import Person


class VoteAction(ChooseAction):
    candidate: Optional[Union[Person, List[Person]]] = None
