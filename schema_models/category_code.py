from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.category_code_set import CategoryCodeSet
from schema_models.defined_term import DefinedTerm


@dataclass
class CategoryCode(DefinedTerm):
    """
    A Category Code.
    """

    codeValue: Optional[Union[str, List[str]]] = None
    inCodeSet: Optional[
        Union[CategoryCodeSet, List[CategoryCodeSet], HttpUrl, List[HttpUrl]]
    ] = None
