from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class Article(CreativeWork):
    """
    An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

    See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """

    articleBody: Optional[Union[str, List[str]]] = None
    articleSection: Optional[Union[str, List[str]]] = None
    backstory: Optional[Union[CreativeWork, List[CreativeWork], str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int], str, List[str]]] = None
    pageStart: Optional[Union[int, List[int], str, List[str]]] = None
    pagination: Optional[Union[str, List[str]]] = None
    speakable: Optional[
        Union[
            "SpeakableSpecification",
            List["SpeakableSpecification"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    wordCount: Optional[Union[int, List[int]]] = None
