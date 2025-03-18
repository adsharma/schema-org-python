from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.organization import Organization


class SportsOrganization(Organization):
    """
    Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """

    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
