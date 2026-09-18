from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization


@dataclass
class MediaSubscription(Intangible):
    """
    A subscription which allows a user to access media including audio, video, books, etc.
    """

    authenticator: Optional[Union[Organization, List[Organization]]] = None
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = None
