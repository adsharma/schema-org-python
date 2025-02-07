from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.country import Country
from schema_models.creative_work import CreativeWork
from schema_models.t_v_series import TVSeries
from schema_models.text import Text
from schema_models.url import URL


class TVSeason(CreativeWork):
    titleEIDR: Optional[Union[Text, List[Text]]] = None
    titleEIDR: Optional[Union[URL, List[URL]]] = None
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
    countryOfOrigin: Optional[Union[Country, List[Country]]] = None
