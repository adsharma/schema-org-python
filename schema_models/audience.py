from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class Audience(Intangible):
    """
    An intended audience, i.e. a group for whom something was created.
    """

    audienceType: Optional[Union[str, List[str]]] = None
    geographicArea: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
