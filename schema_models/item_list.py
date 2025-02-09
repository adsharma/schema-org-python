from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class ItemList(Intangible):
    itemListElement: Optional[Union["ListItem", List["ListItem"]]] = None
    itemListElement: Optional[Union[Thing, List[Thing]]] = None
    itemListElement: Optional[Union[str, List[str]]] = None
    numberOfItems: Optional[Union[int, List[int]]] = None
    itemListOrder: Optional[Union["ItemListOrderType", List["ItemListOrderType"]]] = (
        None
    )
    itemListOrder: Optional[Union[str, List[str]]] = None
