from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.service import Service


class WebAPI(Service):
    """
    An application programming interface accessible over Web/Internet technologies.
    """

    documentation: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
