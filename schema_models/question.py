from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList


class Question(Comment):
    """
    A sub property of object. A question.
    """

    acceptedAnswer: Optional[Union["Answer", List["Answer"]]] = None
    acceptedAnswer: Optional[Union[ItemList, List[ItemList]]] = None
    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union[Comment, List[Comment]]] = None
    suggestedAnswer: Optional[Union["Answer", List["Answer"]]] = None
    suggestedAnswer: Optional[Union[ItemList, List[ItemList]]] = None
    answerCount: Optional[Union[int, List[int]]] = None
    eduQuestionType: Optional[Union[str, List[str]]] = None
