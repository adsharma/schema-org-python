from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.thing import Thing
from schema_models.update_action import UpdateAction


class ReplaceAction(UpdateAction):
    replacee: Optional[Union[Thing, List[Thing]]] = None
    replacer: Optional[Union[Thing, List[Thing]]] = None
