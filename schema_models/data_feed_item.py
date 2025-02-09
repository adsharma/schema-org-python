from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class DataFeedItem(Intangible):
    item: Optional[Union[Thing, List[Thing]]] = None
    dateDeleted: Optional[Union[datetime, List[datetime]]] = None
    dateDeleted: Optional[Union[date, List[date]]] = None
    dateCreated: Optional[Union[datetime, List[datetime]]] = None
    dateCreated: Optional[Union[date, List[date]]] = None
    dateModified: Optional[Union[date, List[date]]] = None
    dateModified: Optional[Union[datetime, List[datetime]]] = None
