from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.speakable_specification import SpeakableSpecification


class Article(CreativeWork):
    """
    An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

    See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).
    """

    pageStart: Optional[Union[str, List[str], int, List[int]]] = None
    speakable: Optional[
        Union[
            HttpUrl, List[HttpUrl], SpeakableSpecification, List[SpeakableSpecification]
        ]
    ] = None
    articleSection: Optional[Union[str, List[str]]] = None
    pagination: Optional[Union[str, List[str]]] = None
    wordCount: Optional[Union[int, List[int]]] = None
    articleBody: Optional[Union[str, List[str]]] = None
    backstory: Optional[Union[CreativeWork, List[CreativeWork], str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int], str, List[str]]] = None
