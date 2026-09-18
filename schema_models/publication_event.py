from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class PublicationEvent(Event):
    """
    A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.
    """

    free: Optional[Union[bool, List[bool]]] = None
    publishedBy: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    publishedOn: Optional[Union["BroadcastService", List["BroadcastService"]]] = None
