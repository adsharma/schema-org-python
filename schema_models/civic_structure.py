from typing import List, Optional, Union

from schema_models.place import Place
from schema_models.text import Text


class CivicStructure(Place):
    openingHours: Optional[Union[Text, List[Text]]] = None
