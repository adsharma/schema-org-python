from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList
from schema_models.list_item import ListItem


class HowToSection(ListItem):
    steps: Optional[Union[ItemList, List[ItemList]]] = None
    steps: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    steps: Optional[Union[str, List[str]]] = None
