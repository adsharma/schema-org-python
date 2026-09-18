from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.answer import Answer
from schema_models.comment import Comment
from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList


@dataclass
class Question(Comment):
    """
    A sub property of object. A question.
    """

    acceptedAnswer: Optional[Union[Answer, List[Answer], ItemList, List[ItemList]]] = (
        None
    )
    answerCount: Optional[Union[int, List[int]]] = None
    eduQuestionType: Optional[Union[str, List[str]]] = None
    parentItem: Optional[
        Union[Comment, List[Comment], CreativeWork, List[CreativeWork]]
    ] = None
    suggestedAnswer: Optional[Union[Answer, List[Answer], ItemList, List[ItemList]]] = (
        None
    )
