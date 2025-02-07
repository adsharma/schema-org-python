from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.text import Text
from schema_models.thing import Thing


class ListItem(Intangible):
    position: Optional[Union[Text, List[Text]]] = None
    position: Optional[Union[Integer, List[Integer]]] = None
    previousItem: Optional[Union["ListItem", List["ListItem"]]] = None
    item: Optional[Union[Thing, List[Thing]]] = None
    nextItem: Optional[Union["ListItem", List["ListItem"]]] = None
