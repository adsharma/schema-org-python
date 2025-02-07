from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.text import Text


class Corporation(Organization):
    tickerSymbol: Optional[Union[Text, List[Text]]] = None
