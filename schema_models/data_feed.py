from typing import List, Optional, Union

from schema_models.data_feed_item import DataFeedItem
from schema_models.dataset import Dataset
from schema_models.thing import Thing


class DataFeed(Dataset):
    """
    A single feed providing structured information about one or more entities or topics.
    """

    dataFeedElement: Optional[
        Union[Thing, List[Thing], str, List[str], DataFeedItem, List[DataFeedItem]]
    ] = None
