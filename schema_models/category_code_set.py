from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.defined_term_set import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """
    A set of Category Code values.
    """

    hasCategoryCode: Optional[Union[CategoryCode, List[CategoryCode]]] = None
