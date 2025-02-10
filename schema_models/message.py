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

    bccRecipient: Optional[Union[Person, List[Person]]] = None
    bccRecipient: Optional[Union[Organization, List[Organization]]] = None
    bccRecipient: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    dateSent: Optional[Union[datetime, List[datetime]]] = None
    messageAttachment: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    recipient: Optional[Union[Audience, List[Audience]]] = None
    recipient: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    recipient: Optional[Union[Person, List[Person]]] = None
    recipient: Optional[Union[Organization, List[Organization]]] = None
    toRecipient: Optional[Union[Audience, List[Audience]]] = None
    toRecipient: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    toRecipient: Optional[Union[Person, List[Person]]] = None
    toRecipient: Optional[Union[Organization, List[Organization]]] = None
    sender: Optional[Union[Organization, List[Organization]]] = None
    sender: Optional[Union[Audience, List[Audience]]] = None
    sender: Optional[Union[Person, List[Person]]] = None
    dateReceived: Optional[Union[datetime, List[datetime]]] = None
    ccRecipient: Optional[Union[Person, List[Person]]] = None
    ccRecipient: Optional[Union[Organization, List[Organization]]] = None
    ccRecipient: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    dateRead: Optional[Union[datetime, List[datetime]]] = None
    dateRead: Optional[Union[date, List[date]]] = None
