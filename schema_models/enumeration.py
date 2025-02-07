from typing import List, Optional, Union

from schema_models.intangible import Intangible


class Enumeration(Intangible):
    supersededBy: Optional[Union["Property", List["Property"]]] = None
    supersededBy: Optional[Union["_Class", List["_Class"]]] = None
    supersededBy: Optional[Union["Enumeration", List["Enumeration"]]] = None
