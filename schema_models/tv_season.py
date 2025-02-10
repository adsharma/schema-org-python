from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.tv_series import TVSeries


class TVSeason(CreativeWork):
    """
    Season dedicated to TV broadcast and associated online delivery.
    """

    titleEIDR: Optional[Union[str, List[str]]] = None
    titleEIDR: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
