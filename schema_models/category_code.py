from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.text import Text
from schema_models.url import URL


class CategoryCode(DefinedTerm):
    inCodeSet: Optional[Union[URL, List[URL]]] = None
    inCodeSet: Optional[Union["CategoryCodeSet", List["CategoryCodeSet"]]] = None
    codeValue: Optional[Union[Text, List[Text]]] = None
