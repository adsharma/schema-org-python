from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.organize_action import OrganizeAction


class PlanAction(OrganizeAction):
    scheduledTime: Optional[Union[DateTime, List[DateTime]]] = None
    scheduledTime: Optional[Union[Date, List[Date]]] = None
