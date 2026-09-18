from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class PublicationIssue(CreativeWork):
    """
    A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.

    See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """

    issueNumber: Optional[Union[int, List[int], str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int], str, List[str]]] = None
    pageStart: Optional[Union[int, List[int], str, List[str]]] = None
    pagination: Optional[Union[str, List[str]]] = None
