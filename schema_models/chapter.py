from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.text import Text


class Chapter(CreativeWork):
    pageEnd: Optional[Union[Integer, List[Integer]]] = None
    pageEnd: Optional[Union[Text, List[Text]]] = None
    pageStart: Optional[Union[Text, List[Text]]] = None
    pageStart: Optional[Union[Integer, List[Integer]]] = None
    pagination: Optional[Union[Text, List[Text]]] = None
