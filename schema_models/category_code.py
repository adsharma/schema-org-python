from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm


@dataclass
class CategoryCode(DefinedTerm):
    """
    A Category Code.
    """

    inCodeSet: Optional[
        Union[HttpUrl, List[HttpUrl], "CategoryCodeSet", List["CategoryCodeSet"]]
    ] = None
    codeValue: Optional[Union[str, List[str]]] = None
