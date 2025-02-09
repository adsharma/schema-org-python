from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.person import Person


class PublicationEvent(Event):
    publishedBy: Optional[Union[Person, List[Person]]] = None
    publishedBy: Optional[Union[Organization, List[Organization]]] = None
    publishedOn: Optional[Union["BroadcastService", List["BroadcastService"]]] = None
    free: Optional[Union[bool, List[bool]]] = None
