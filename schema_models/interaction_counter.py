from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.date_time import DateTime
from schema_models.integer import Integer
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.software_application import SoftwareApplication
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.time import Time
from schema_models.virtual_location import VirtualLocation
from schema_models.web_site import WebSite


class InteractionCounter(StructuredValue):
    userInteractionCount: Optional[Union[Integer, List[Integer]]] = None
    endTime: Optional[Union[DateTime, List[DateTime]]] = None
    endTime: Optional[Union[Time, List[Time]]] = None
    location: Optional[Union[Text, List[Text]]] = None
    location: Optional[Union[Place, List[Place]]] = None
    location: Optional[Union[VirtualLocation, List[VirtualLocation]]] = None
    location: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    startTime: Optional[Union[DateTime, List[DateTime]]] = None
    startTime: Optional[Union[Time, List[Time]]] = None
    interactionType: Optional[Union[Action, List[Action]]] = None
    interactionService: Optional[Union[WebSite, List[WebSite]]] = None
    interactionService: Optional[
        Union[SoftwareApplication, List[SoftwareApplication]]
    ] = None
