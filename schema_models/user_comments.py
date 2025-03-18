from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.user_interaction import UserInteraction


class UserComments(UserInteraction):
    """
    UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """

    replyToUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    commentTime: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    creator: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    commentText: Optional[Union[str, List[str]]] = None
    discusses: Optional[Union[CreativeWork, List[CreativeWork]]] = None
