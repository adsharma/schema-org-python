from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.data_feed import DataFeed
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class PodcastSeries(CreativeWorkSeries):
    webFeed: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    webFeed: Optional[Union[DataFeed, List[DataFeed]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
