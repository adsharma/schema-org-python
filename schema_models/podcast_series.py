from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person


@dataclass
class PodcastSeries(CreativeWorkSeries):
    """
    A podcast is an episodic series of digital audio or video files which a user can download and listen to.
    """

    actor: Optional[
        Union[PerformingGroup, List[PerformingGroup], Person, List[Person]]
    ] = None
    webFeed: Optional[Union["DataFeed", List["DataFeed"], HttpUrl, List[HttpUrl]]] = (
        None
    )
