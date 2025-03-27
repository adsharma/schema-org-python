from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class Audience(Intangible):
    """
    Intended audience for an item, i.e. the group for whom the item was created.
    """

    audienceType: Optional[Union[str, List[str]]] = None
    geographicArea: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
