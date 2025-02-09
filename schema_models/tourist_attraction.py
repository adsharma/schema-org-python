from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.place import Place


class TouristAttraction(Place):
    touristType: Optional[Union[str, List[str]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
