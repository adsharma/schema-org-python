from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.data_feed import DataFeed
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.url import URL


class PodcastSeries(CreativeWorkSeries):
    webFeed: Optional[Union[URL, List[URL]]] = None
    webFeed: Optional[Union[DataFeed, List[DataFeed]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
