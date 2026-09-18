from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


@dataclass
class DataFeedItem(Intangible):
    """
    A single item within a larger data feed.
    """

    dateCreated: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    dateDeleted: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    dateModified: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    item: Optional[Union[Thing, List[Thing]]] = None
