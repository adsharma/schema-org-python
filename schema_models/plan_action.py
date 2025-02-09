from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.organize_action import OrganizeAction


class PlanAction(OrganizeAction):
    scheduledTime: Optional[Union[datetime, List[datetime]]] = None
    scheduledTime: Optional[Union[date, List[date]]] = None
