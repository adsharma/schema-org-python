from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.distance import Distance
from schema_models.move_action import MoveAction


class TravelAction(MoveAction):
    distance: Optional[Union[Distance, List[Distance]]] = None
