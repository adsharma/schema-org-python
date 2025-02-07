from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.thing import Thing


class UpdateAction(Action):
    collection: Optional[Union[Thing, List[Thing]]] = None
    targetCollection: Optional[Union[Thing, List[Thing]]] = None
