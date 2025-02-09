from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class CreativeWorkSeries(CreativeWork):
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    issn: Optional[Union[str, List[str]]] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
