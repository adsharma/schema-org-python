from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class PublicationVolume(CreativeWork):
    """
    A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.

    See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).
    """

    pagination: Optional[Union[str, List[str]]] = None
    volumeNumber: Optional[Union[str, List[str]]] = None
    volumeNumber: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
