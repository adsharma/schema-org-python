from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


@dataclass
class Action(Thing):
    """
    An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.

    See also [blog post](https://blog.schema.org/2014/04/16/announcing-schema-org-actions/) and [Actions overview document](https://schema.org/docs/actions.html).
    """

    actionProcess: Optional[Union["HowTo", List["HowTo"]]] = None
    actionStatus: Optional[Union["ActionStatusType", List["ActionStatusType"]]] = None
    agent: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    error: Optional[Union[Thing, List[Thing]]] = None
    instrument: Optional[Union[Thing, List[Thing]]] = None
    location: Optional[
        Union[
            "Place",
            List["Place"],
            "PostalAddress",
            List["PostalAddress"],
            str,
            List[str],
            "VirtualLocation",
            List["VirtualLocation"],
        ]
    ] = None
    object: Optional[Union[Thing, List[Thing]]] = None
    participant: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    provider: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    result: Optional[Union[Thing, List[Thing]]] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    target: Optional[
        Union["EntryPoint", List["EntryPoint"], HttpUrl, List[HttpUrl]]
    ] = None
