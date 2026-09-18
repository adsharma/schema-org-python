from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class PublicationVolume(CreativeWork):
    """
    A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.

    See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """

    pageEnd: Optional[Union[int, List[int], str, List[str]]] = None
    pageStart: Optional[Union[int, List[int], str, List[str]]] = None
    pagination: Optional[Union[str, List[str]]] = None
    volumeNumber: Optional[Union[int, List[int], str, List[str]]] = None
