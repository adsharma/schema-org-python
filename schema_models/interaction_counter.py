from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.place import Place
from schema_models.software_application import SoftwareApplication
from schema_models.structured_value import StructuredValue
from schema_models.virtual_location import VirtualLocation
from schema_models.web_site import WebSite


class InteractionCounter(StructuredValue):
    """
    A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.
    """

    userInteractionCount: Optional[Union[int, List[int]]] = None
    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    location: Optional[
        Union[
            str,
            List[str],
            Place,
            List[Place],
            VirtualLocation,
            List[VirtualLocation],
            "PostalAddress",
            List["PostalAddress"],
        ]
    ] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    interactionType: Optional[Union[Action, List[Action]]] = None
    interactionService: Optional[
        Union[WebSite, List[WebSite], SoftwareApplication, List[SoftwareApplication]]
    ] = None
