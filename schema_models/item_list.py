from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class ItemList(Intangible):
    """
    A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.
    """

    itemListElement: Optional[Union["ListItem", List["ListItem"]]] = None
    itemListElement: Optional[Union[Thing, List[Thing]]] = None
    itemListElement: Optional[Union[str, List[str]]] = None
    numberOfItems: Optional[Union[int, List[int]]] = None
    itemListOrder: Optional[Union["ItemListOrderType", List["ItemListOrderType"]]] = (
        None
    )
    itemListOrder: Optional[Union[str, List[str]]] = None
