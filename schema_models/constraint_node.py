from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.url import URL


class ConstraintNode(Intangible):
    numConstraints: Optional[Union[Integer, List[Integer]]] = None
    constraintProperty: Optional[Union["Property", List["Property"]]] = None
    constraintProperty: Optional[Union[URL, List[URL]]] = None
