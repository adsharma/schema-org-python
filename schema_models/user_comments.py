from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.user_interaction import UserInteraction


class UserComments(UserInteraction):
    replyToUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    commentTime: Optional[Union[datetime, List[datetime]]] = None
    commentTime: Optional[Union[date, List[date]]] = None
    creator: Optional[Union[Person, List[Person]]] = None
    creator: Optional[Union[Organization, List[Organization]]] = None
    commentText: Optional[Union[str, List[str]]] = None
    discusses: Optional[Union[CreativeWork, List[CreativeWork]]] = None
