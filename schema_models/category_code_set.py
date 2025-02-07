from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.category_code import CategoryCode
from schema_models.defined_term_set import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    hasCategoryCode: Optional[Union[CategoryCode, List[CategoryCode]]] = None
