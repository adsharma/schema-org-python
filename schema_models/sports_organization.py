from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.organization import Organization


class SportsOrganization(Organization):
    sport: Optional[Union[str, List[str]]] = None
    sport: Optional[Union[HttpUrl, List[HttpUrl]]] = None
