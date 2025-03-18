from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList
from schema_models.list_item import ListItem


class HowToSection(ListItem):
    """
    A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).
    """

    steps: Optional[
        Union[
            ItemList, List[ItemList], CreativeWork, List[CreativeWork], str, List[str]
        ]
    ] = None
