from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class DataFeedItem(Intangible):
    """
    A single item within a larger data feed.
    """

    item: Optional[Union[Thing, List[Thing]]] = None
    dateDeleted: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    dateCreated: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    dateModified: Optional[Union[date, List[date], datetime, List[datetime]]] = None
