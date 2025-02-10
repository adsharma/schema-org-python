from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Map(CreativeWork):
    """
    A map.
    """

    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = None
