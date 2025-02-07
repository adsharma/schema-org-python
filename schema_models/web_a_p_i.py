from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.service import Service
from schema_models.url import URL


class WebAPI(Service):
    documentation: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    documentation: Optional[Union[URL, List[URL]]] = None
