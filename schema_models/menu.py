from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.menu_item import MenuItem


class Menu(CreativeWork):
    """
    A structured representation of food or drink items available from a FoodEstablishment.
    """

    hasMenuItem: Optional[Union[MenuItem, List[MenuItem]]] = None
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = None
