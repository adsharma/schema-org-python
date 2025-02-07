from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.text import Text


class Audience(Intangible):
    audienceType: Optional[Union[Text, List[Text]]] = None
    geographicArea: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
