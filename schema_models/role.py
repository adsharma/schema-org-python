from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class Role(Intangible):
    roleName: Optional[Union[Text, List[Text]]] = None
    roleName: Optional[Union[URL, List[URL]]] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    namedPosition: Optional[Union[Text, List[Text]]] = None
    namedPosition: Optional[Union[URL, List[URL]]] = None
