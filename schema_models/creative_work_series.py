from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.text import Text


class CreativeWorkSeries(CreativeWork):
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    issn: Optional[Union[Text, List[Text]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
