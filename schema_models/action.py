from datetime import datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.organization import Organization
from schema_models.thing import Thing


class Action(Thing):
    participant: Optional[Union["Person", List["Person"]]] = None
    participant: Optional[Union[Organization, List[Organization]]] = None
    provider: Optional[Union["Person", List["Person"]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    error: Optional[Union[Thing, List[Thing]]] = None
    location: Optional[Union[str, List[str]]] = None
    location: Optional[Union["Place", List["Place"]]] = None
    location: Optional[Union["VirtualLocation", List["VirtualLocation"]]] = None
    location: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    result: Optional[Union[Thing, List[Thing]]] = None
    startTime: Optional[Union[datetime, List[datetime]]] = None
    startTime: Optional[Union[time, List[time]]] = None
    actionStatus: Optional[Union["ActionStatusType", List["ActionStatusType"]]] = None
    instrument: Optional[Union[Thing, List[Thing]]] = None
    actionProcess: Optional[Union["HowTo", List["HowTo"]]] = None
    endTime: Optional[Union[datetime, List[datetime]]] = None
    endTime: Optional[Union[time, List[time]]] = None
    target: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    target: Optional[Union["EntryPoint", List["EntryPoint"]]] = None
    object: Optional[Union[Thing, List[Thing]]] = None
    agent: Optional[Union["Person", List["Person"]]] = None
    agent: Optional[Union[Organization, List[Organization]]] = None
