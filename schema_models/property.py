from typing import List, Optional, Union

from schema_models.enumeration import Enumeration
from schema_models.intangible import Intangible


class Property(Intangible):
    rangeIncludes: Optional[Union["_Class", List["_Class"]]] = None
    domainIncludes: Optional[Union["_Class", List["_Class"]]] = None
    supersededBy: Optional[Union["Property", List["Property"]]] = None
    supersededBy: Optional[Union["_Class", List["_Class"]]] = None
    supersededBy: Optional[Union[Enumeration, List[Enumeration]]] = None
    inverseOf: Optional[Union["Property", List["Property"]]] = None
