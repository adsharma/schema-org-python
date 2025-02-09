from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class ConstraintNode(Intangible):
    numConstraints: Optional[Union[int, List[int]]] = None
    constraintProperty: Optional[Union["Property", List["Property"]]] = None
    constraintProperty: Optional[Union[HttpUrl, List[HttpUrl]]] = None
