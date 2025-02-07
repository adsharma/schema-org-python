from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.react_action import ReactAction


class EndorseAction(ReactAction):
    endorsee: Optional[Union[Person, List[Person]]] = None
    endorsee: Optional[Union[Organization, List[Organization]]] = None
