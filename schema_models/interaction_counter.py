from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.place import Place
from schema_models.software_application import SoftwareApplication
from schema_models.structured_value import StructuredValue
from schema_models.virtual_location import VirtualLocation
from schema_models.web_site import WebSite


class InteractionCounter(StructuredValue):
    userInteractionCount: Optional[Union[int, List[int]]] = None
    endTime: Optional[Union[datetime, List[datetime]]] = None
    endTime: Optional[Union[time, List[time]]] = None
    location: Optional[Union[str, List[str]]] = None
    location: Optional[Union[Place, List[Place]]] = None
    location: Optional[Union[VirtualLocation, List[VirtualLocation]]] = None
    location: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    startTime: Optional[Union[datetime, List[datetime]]] = None
    startTime: Optional[Union[time, List[time]]] = None
    interactionType: Optional[Union[Action, List[Action]]] = None
    interactionService: Optional[Union[WebSite, List[WebSite]]] = None
    interactionService: Optional[
        Union[SoftwareApplication, List[SoftwareApplication]]
    ] = None
