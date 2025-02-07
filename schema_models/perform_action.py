from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.entertainment_business import EntertainmentBusiness
from schema_models.play_action import PlayAction


class PerformAction(PlayAction):
    entertainmentBusiness: Optional[
        Union[EntertainmentBusiness, List[EntertainmentBusiness]]
    ] = None
