from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class Menu(CreativeWork):
    """
    Either the actual menu as a structured representation, as text, or a URL of the menu.
    """

    hasMenuItem: Optional[Union["MenuItem", List["MenuItem"]]] = None
    hasMenuSection: Optional[Union["MenuSection", List["MenuSection"]]] = None
