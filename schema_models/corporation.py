from typing import List, Optional, Union

from schema_models.organization import Organization


class Corporation(Organization):
    """
    Organization: A business corporation.
    """

    tickerSymbol: Optional[Union[str, List[str]]] = None
