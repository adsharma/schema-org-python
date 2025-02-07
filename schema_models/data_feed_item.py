from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.thing import Thing


class DataFeedItem(Intangible):
    item: Optional[Union[Thing, List[Thing]]] = None
    dateDeleted: Optional[Union[DateTime, List[DateTime]]] = None
    dateDeleted: Optional[Union[Date, List[Date]]] = None
    dateCreated: Optional[Union[DateTime, List[DateTime]]] = None
    dateCreated: Optional[Union[Date, List[Date]]] = None
    dateModified: Optional[Union[Date, List[Date]]] = None
    dateModified: Optional[Union[DateTime, List[DateTime]]] = None
