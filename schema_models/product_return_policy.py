from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class ProductReturnPolicy(Intangible):
    """
    A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]].
    """

    productReturnDays: Optional[Union[int, List[int]]] = None
    productReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
