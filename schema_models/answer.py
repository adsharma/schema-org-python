from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.creative_work import CreativeWork
from schema_models.web_content import WebContent


class Answer(Comment):
    """
    An answer offered to a question; perhaps correct, perhaps opinionated or wrong.
    """

    answerExplanation: Optional[
        Union[Comment, List[Comment], WebContent, List[WebContent]]
    ] = None
    parentItem: Optional[
        Union[CreativeWork, List[CreativeWork], Comment, List[Comment]]
    ] = None
