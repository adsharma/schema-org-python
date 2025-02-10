from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Chapter(CreativeWork):
    """
    One of the sections into which a book is divided. A chapter usually has a section number or a name.
    """

    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
    pagination: Optional[Union[str, List[str]]] = None
