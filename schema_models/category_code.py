from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.category_code_set import CategoryCodeSet
from schema_models.defined_term import DefinedTerm
from schema_models.text import Text
from schema_models.url import URL


class CategoryCode(DefinedTerm):
    inCodeSet: Optional[Union[URL, List[URL]]] = None
    inCodeSet: Optional[Union[CategoryCodeSet, List[CategoryCodeSet]]] = None
    codeValue: Optional[Union[Text, List[Text]]] = None
