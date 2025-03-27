from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization


@dataclass
class Corporation(Organization):
    """
    Organization: A business corporation.
    """

    tickerSymbol: Optional[Union[str, List[str]]] = None
