from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.text import Text
from schema_models.url import URL


class SportsOrganization(Organization):
    sport: Optional[Union[Text, List[Text]]] = None
    sport: Optional[Union[URL, List[URL]]] = None
