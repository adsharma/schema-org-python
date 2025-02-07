from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.item_list_order_type import ItemListOrderType
from schema_models.list_item import ListItem
from schema_models.text import Text
from schema_models.thing import Thing


class ItemList(Intangible):
    itemListElement: Optional[Union[ListItem, List[ListItem]]] = None
    itemListElement: Optional[Union[Thing, List[Thing]]] = None
    itemListElement: Optional[Union[Text, List[Text]]] = None
    numberOfItems: Optional[Union[Integer, List[Integer]]] = None
    itemListOrder: Optional[Union[ItemListOrderType, List[ItemListOrderType]]] = None
    itemListOrder: Optional[Union[Text, List[Text]]] = None
