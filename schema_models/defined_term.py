from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class DefinedTerm(Intangible):
    inDefinedTermSet: Optional[Union[URL, List[URL]]] = None
    inDefinedTermSet: Optional[Union["DefinedTermSet", List["DefinedTermSet"]]] = None
    termCode: Optional[Union[Text, List[Text]]] = None
