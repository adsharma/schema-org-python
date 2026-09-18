from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.episode import Episode
from schema_models.language import Language
from schema_models.tv_series import TVSeries


@dataclass
class TVEpisode(Episode):
    """
    A TV episode which can be part of a series or season.
    """

    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
