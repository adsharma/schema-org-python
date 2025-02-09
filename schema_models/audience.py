from typing import List, Optional, Union

from schema_models.intangible import Intangible


class Audience(Intangible):
    audienceType: Optional[Union[str, List[str]]] = None
    geographicArea: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
