from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class DefinedTerm(Intangible):
    inDefinedTermSet: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    inDefinedTermSet: Optional[Union["DefinedTermSet", List["DefinedTermSet"]]] = None
    termCode: Optional[Union[str, List[str]]] = None
