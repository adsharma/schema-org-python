from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class ProductReturnPolicy(Intangible):
    productReturnDays: Optional[Union[int, List[int]]] = None
    productReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
