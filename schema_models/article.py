from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.speakable_specification import SpeakableSpecification
from schema_models.text import Text
from schema_models.url import URL


class Article(CreativeWork):
    pageStart: Optional[Union[Text, List[Text]]] = None
    pageStart: Optional[Union[Integer, List[Integer]]] = None
    speakable: Optional[Union[URL, List[URL]]] = None
    speakable: Optional[Union[SpeakableSpecification, List[SpeakableSpecification]]] = (
        None
    )
    articleSection: Optional[Union[Text, List[Text]]] = None
    pagination: Optional[Union[Text, List[Text]]] = None
    wordCount: Optional[Union[Integer, List[Integer]]] = None
    articleBody: Optional[Union[Text, List[Text]]] = None
    backstory: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    backstory: Optional[Union[Text, List[Text]]] = None
    pageEnd: Optional[Union[Integer, List[Integer]]] = None
    pageEnd: Optional[Union[Text, List[Text]]] = None
