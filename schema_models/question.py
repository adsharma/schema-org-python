from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.answer import Answer
from schema_models.comment import Comment
from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.item_list import ItemList
from schema_models.text import Text


class Question(Comment):
    acceptedAnswer: Optional[Union[Answer, List[Answer]]] = None
    acceptedAnswer: Optional[Union[ItemList, List[ItemList]]] = None
    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union[Comment, List[Comment]]] = None
    suggestedAnswer: Optional[Union[Answer, List[Answer]]] = None
    suggestedAnswer: Optional[Union[ItemList, List[ItemList]]] = None
    answerCount: Optional[Union[Integer, List[Integer]]] = None
    eduQuestionType: Optional[Union[Text, List[Text]]] = None
