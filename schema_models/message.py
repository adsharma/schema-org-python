from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Message(CreativeWork):
    """
    A single message from a sender to one or more organizations or people.
    """

    bccRecipient: Optional[
        Union[
            Person,
            List[Person],
            Organization,
            List[Organization],
            "ContactPoint",
            List["ContactPoint"],
        ]
    ] = None
    dateSent: Optional[Union[datetime, List[datetime]]] = None
    messageAttachment: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Person,
            List[Person],
            Organization,
            List[Organization],
        ]
    ] = None
    toRecipient: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Person,
            List[Person],
            Organization,
            List[Organization],
        ]
    ] = None
    sender: Optional[
        Union[
            Organization,
            List[Organization],
            Audience,
            List[Audience],
            Person,
            List[Person],
        ]
    ] = None
    dateReceived: Optional[Union[datetime, List[datetime]]] = None
    ccRecipient: Optional[
        Union[
            Person,
            List[Person],
            Organization,
            List[Organization],
            "ContactPoint",
            List["ContactPoint"],
        ]
    ] = None
    dateRead: Optional[Union[datetime, List[datetime], date, List[date]]] = None
