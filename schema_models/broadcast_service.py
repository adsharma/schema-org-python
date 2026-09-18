from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.broadcast_channel import BroadcastChannel
from schema_models.broadcast_frequency_specification import (
    BroadcastFrequencySpecification,
)
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.service import Service


@dataclass
class BroadcastService(Service):
    """
    A delivery service through which content is provided via broadcast over the air or online.
    """

    area: Optional[Union[Place, List[Place]]] = None
    broadcastAffiliateOf: Optional[Union[Organization, List[Organization]]] = None
    broadcastDisplayName: Optional[Union[str, List[str]]] = None
    broadcastFrequency: Optional[
        Union[
            BroadcastFrequencySpecification,
            List[BroadcastFrequencySpecification],
            str,
            List[str],
        ]
    ] = None
    broadcastTimezone: Optional[Union[str, List[str]]] = None
    broadcaster: Optional[Union[Organization, List[Organization]]] = None
    callSign: Optional[Union[str, List[str]]] = None
    hasBroadcastChannel: Optional[Union[BroadcastChannel, List[BroadcastChannel]]] = (
        None
    )
    inLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    parentService: Optional[Union["BroadcastService", List["BroadcastService"]]] = None
    videoFormat: Optional[Union[str, List[str]]] = None
