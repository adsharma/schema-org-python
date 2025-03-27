from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class Enumeration(Intangible):
    """
    Lists or enumerations—for example, a list of cuisines or music genres, etc.
    """

    supersededBy: Optional[
        Union[
            "Property",
            List["Property"],
            "_Class",
            List["_Class"],
            "Enumeration",
            List["Enumeration"],
        ]
    ] = None
