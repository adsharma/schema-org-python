from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.online_store import OnlineStore


@dataclass
class OnlineMarketplace(OnlineStore):
    """
    An eCommerce marketplace.
    """

    hasStore: Optional[Union[OnlineStore, List[OnlineStore]]] = None
