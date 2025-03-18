from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.country import Country
from schema_models.episode import Episode
from schema_models.language import Language
from schema_models.tv_series import TVSeries


class TVEpisode(Episode):
    """
    A TV episode which can be part of a series or season.
    """

    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union[Country, List[Country]]] = None
    subtitleLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
