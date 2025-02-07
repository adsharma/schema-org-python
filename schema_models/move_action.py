from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.place import Place


class MoveAction(Action):
    fromLocation: Optional[Union[Place, List[Place]]] = None
    toLocation: Optional[Union[Place, List[Place]]] = None
