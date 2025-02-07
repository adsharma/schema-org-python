from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action_status_type import ActionStatusType
from schema_models.date_time import DateTime
from schema_models.entry_point import EntryPoint
from schema_models.how_to import HowTo
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.time import Time
from schema_models.url import URL
from schema_models.virtual_location import VirtualLocation


class Action(Thing):
    participant: Optional[Union[Person, List[Person]]] = None
    participant: Optional[Union[Organization, List[Organization]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    error: Optional[Union[Thing, List[Thing]]] = None
    location: Optional[Union[Text, List[Text]]] = None
    location: Optional[Union[Place, List[Place]]] = None
    location: Optional[Union[VirtualLocation, List[VirtualLocation]]] = None
    location: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    result: Optional[Union[Thing, List[Thing]]] = None
    startTime: Optional[Union[DateTime, List[DateTime]]] = None
    startTime: Optional[Union[Time, List[Time]]] = None
    actionStatus: Optional[Union[ActionStatusType, List[ActionStatusType]]] = None
    instrument: Optional[Union[Thing, List[Thing]]] = None
    actionProcess: Optional[Union[HowTo, List[HowTo]]] = None
    endTime: Optional[Union[DateTime, List[DateTime]]] = None
    endTime: Optional[Union[Time, List[Time]]] = None
    target: Optional[Union[URL, List[URL]]] = None
    target: Optional[Union[EntryPoint, List[EntryPoint]]] = None
    object: Optional[Union[Thing, List[Thing]]] = None
    agent: Optional[Union[Person, List[Person]]] = None
    agent: Optional[Union[Organization, List[Organization]]] = None
