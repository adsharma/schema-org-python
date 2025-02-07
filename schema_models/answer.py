from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.creative_work import CreativeWork
from schema_models.web_content import WebContent


class Answer(Comment):
    answerExplanation: Optional[Union[Comment, List[Comment]]] = None
    answerExplanation: Optional[Union[WebContent, List[WebContent]]] = None
    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union[Comment, List[Comment]]] = None
