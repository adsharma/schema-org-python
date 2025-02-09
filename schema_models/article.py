from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.speakable_specification import SpeakableSpecification


class Article(CreativeWork):
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
    speakable: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    speakable: Optional[Union[SpeakableSpecification, List[SpeakableSpecification]]] = (
        None
    )
    articleSection: Optional[Union[str, List[str]]] = None
    pagination: Optional[Union[str, List[str]]] = None
    wordCount: Optional[Union[int, List[int]]] = None
    articleBody: Optional[Union[str, List[str]]] = None
    backstory: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    backstory: Optional[Union[str, List[str]]] = None
    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
