from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.online_business import OnlineBusiness


@dataclass
class OnlineStore(OnlineBusiness):
    """
    An eCommerce site.
    """

    isStoreOn: Optional[Union["OnlineMarketplace", List["OnlineMarketplace"]]] = None
