from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MapCategoryType(Enumeration):
    """
    An enumeration of several kinds of Map.
    """
