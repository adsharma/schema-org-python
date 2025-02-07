from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.country import Country
from schema_models.episode import Episode
from schema_models.language import Language
from schema_models.t_v_series import TVSeries
from schema_models.text import Text
from schema_models.url import URL


class TVEpisode(Episode):
    titleEIDR: Optional[Union[Text, List[Text]]] = None
    titleEIDR: Optional[Union[URL, List[URL]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union[Country, List[Country]]] = None
    subtitleLanguage: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language]]] = None
