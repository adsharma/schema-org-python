from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.t_v_series import TVSeries


class TVSeason(CreativeWork):
    titleEIDR: Optional[Union[str, List[str]]] = None
    titleEIDR: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
