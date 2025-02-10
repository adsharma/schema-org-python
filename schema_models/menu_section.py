from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.menu_item import MenuItem


class MenuSection(CreativeWork):
    """
    A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu provider.
    """

    hasMenuItem: Optional[Union[MenuItem, List[MenuItem]]] = None
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = None
