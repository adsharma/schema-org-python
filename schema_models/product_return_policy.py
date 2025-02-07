from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.url import URL


class ProductReturnPolicy(Intangible):
    productReturnDays: Optional[Union[Integer, List[Integer]]] = None
    productReturnLink: Optional[Union[URL, List[URL]]] = None
