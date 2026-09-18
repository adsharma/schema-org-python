from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class Map(CreativeWork):
    """
    A URL to a map of the place.
    """

    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = None
