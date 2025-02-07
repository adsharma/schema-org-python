from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.place import Place
from schema_models.text import Text


class TouristAttraction(Place):
    touristType: Optional[Union[Text, List[Text]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    availableLanguage: Optional[Union[Text, List[Text]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
