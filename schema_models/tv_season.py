from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class TVSeason(CreativeWork):
    """
    Season dedicated to TV broadcast and associated online delivery.
    """

    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    partOfTVSeries: Optional[Union["TVSeries", List["TVSeries"]]] = None
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
