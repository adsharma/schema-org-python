from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.data_feed import DataFeed
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


class PodcastSeries(CreativeWorkSeries):
    """
    A podcast is an episodic series of digital audio or video files which a user can download and listen to.
    """

    webFeed: Optional[Union[HttpUrl, List[HttpUrl], DataFeed, List[DataFeed]]] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
