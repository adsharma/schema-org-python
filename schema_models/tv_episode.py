from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.country import Country
from schema_models.episode import Episode
from schema_models.language import Language
from schema_models.tv_series import TVSeries


class TVEpisode(Episode):
    titleEIDR: Optional[Union[str, List[str]]] = None
    titleEIDR: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union[Country, List[Country]]] = None
    subtitleLanguage: Optional[Union[str, List[str]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language]]] = None
