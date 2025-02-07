from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.text import Text


class PublicationIssue(CreativeWork):
    pagination: Optional[Union[Text, List[Text]]] = None
    pageEnd: Optional[Union[Integer, List[Integer]]] = None
    pageEnd: Optional[Union[Text, List[Text]]] = None
    pageStart: Optional[Union[Text, List[Text]]] = None
    pageStart: Optional[Union[Integer, List[Integer]]] = None
    issueNumber: Optional[Union[Text, List[Text]]] = None
    issueNumber: Optional[Union[Integer, List[Integer]]] = None
