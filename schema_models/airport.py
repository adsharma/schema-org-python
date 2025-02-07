from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure
from schema_models.text import Text


class Airport(CivicStructure):
    iataCode: Optional[Union[Text, List[Text]]] = None
    icaoCode: Optional[Union[Text, List[Text]]] = None
