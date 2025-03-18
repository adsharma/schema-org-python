from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class PublicationIssue(CreativeWork):
    """
    A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.

    See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).
    """

    pagination: Optional[Union[str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int], str, List[str]]] = None
    pageStart: Optional[Union[str, List[str], int, List[int]]] = None
    issueNumber: Optional[Union[str, List[str], int, List[int]]] = None
