from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class PublicationIssue(CreativeWork):
    pagination: Optional[Union[str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
    issueNumber: Optional[Union[str, List[str]]] = None
    issueNumber: Optional[Union[int, List[int]]] = None
