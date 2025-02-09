from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Chapter(CreativeWork):
    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
    pagination: Optional[Union[str, List[str]]] = None
