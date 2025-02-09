from typing import List, Optional, Union

from schema_models.data_feed_item import DataFeedItem
from schema_models.dataset import Dataset
from schema_models.thing import Thing


class DataFeed(Dataset):
    dataFeedElement: Optional[Union[Thing, List[Thing]]] = None
    dataFeedElement: Optional[Union[str, List[str]]] = None
    dataFeedElement: Optional[Union[DataFeedItem, List[DataFeedItem]]] = None
