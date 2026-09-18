from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Message(CreativeWork):
    """
    A single message from a sender to one or more organizations or people.
    """

    bccRecipient: Optional[
        Union[
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
    ccRecipient: Optional[
        Union[
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
    dateRead: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    dateReceived: Optional[Union[datetime, List[datetime]]] = None
    dateSent: Optional[Union[datetime, List[datetime]]] = None
    messageAttachment: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    recipient: Optional[
        Union[
            "Audience",
            List["Audience"],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
    sender: Optional[
        Union[
            "Audience",
            List["Audience"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
    toRecipient: Optional[
        Union[
            "Audience",
            List["Audience"],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
