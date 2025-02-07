from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization


class MediaSubscription(Intangible):
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = None
    authenticator: Optional[Union[Organization, List[Organization]]] = None
