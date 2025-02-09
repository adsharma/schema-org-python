from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class Role(Intangible):
    roleName: Optional[Union[str, List[str]]] = None
    roleName: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
    namedPosition: Optional[Union[str, List[str]]] = None
    namedPosition: Optional[Union[HttpUrl, List[HttpUrl]]] = None
