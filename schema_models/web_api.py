from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.service import Service


class WebAPI(Service):
    documentation: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    documentation: Optional[Union[HttpUrl, List[HttpUrl]]] = None
