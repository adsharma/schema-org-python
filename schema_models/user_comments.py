from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL
from schema_models.user_interaction import UserInteraction


class UserComments(UserInteraction):
    replyToUrl: Optional[Union[URL, List[URL]]] = None
    commentTime: Optional[Union[DateTime, List[DateTime]]] = None
    commentTime: Optional[Union[Date, List[Date]]] = None
    creator: Optional[Union[Person, List[Person]]] = None
    creator: Optional[Union[Organization, List[Organization]]] = None
    commentText: Optional[Union[Text, List[Text]]] = None
    discusses: Optional[Union[CreativeWork, List[CreativeWork]]] = None
