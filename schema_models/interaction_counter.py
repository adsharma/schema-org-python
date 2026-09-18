from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.place import Place
from schema_models.software_application import SoftwareApplication
from schema_models.structured_value import StructuredValue
from schema_models.virtual_location import VirtualLocation
from schema_models.web_site import WebSite


@dataclass
class InteractionCounter(StructuredValue):
    """
    A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.
    """

    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    interactionService: Optional[
        Union[SoftwareApplication, List[SoftwareApplication], WebSite, List[WebSite]]
    ] = None
    interactionType: Optional[Union[Action, List[Action]]] = None
    location: Optional[
        Union[
            Place,
            List[Place],
            "PostalAddress",
            List["PostalAddress"],
            str,
            List[str],
            VirtualLocation,
            List[VirtualLocation],
        ]
    ] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    userInteractionCount: Optional[Union[int, List[int]]] = None
