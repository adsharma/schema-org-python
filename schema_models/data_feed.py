from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.data_feed_item import DataFeedItem
from schema_models.dataset import Dataset
from schema_models.text import Text
from schema_models.thing import Thing


class DataFeed(Dataset):
    dataFeedElement: Optional[Union[Thing, List[Thing]]] = None
    dataFeedElement: Optional[Union[Text, List[Text]]] = None
    dataFeedElement: Optional[Union[DataFeedItem, List[DataFeedItem]]] = None
