from typing import List, Optional, Union

from schema_models.broadcast_channel import BroadcastChannel
from schema_models.broadcast_frequency_specification import (
    BroadcastFrequencySpecification,
)
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.service import Service


class BroadcastService(Service):
    """
    A delivery service through which content is provided via broadcast over the air or online.
    """

    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    broadcaster: Optional[Union[Organization, List[Organization]]] = None
    area: Optional[Union[Place, List[Place]]] = None
    hasBroadcastChannel: Optional[Union[BroadcastChannel, List[BroadcastChannel]]] = (
        None
    )
    callSign: Optional[Union[str, List[str]]] = None
    videoFormat: Optional[Union[str, List[str]]] = None
    broadcastAffiliateOf: Optional[Union[Organization, List[Organization]]] = None
    parentService: Optional[Union["BroadcastService", List["BroadcastService"]]] = None
    broadcastDisplayName: Optional[Union[str, List[str]]] = None
    broadcastTimezone: Optional[Union[str, List[str]]] = None
    broadcastFrequency: Optional[Union[str, List[str]]] = None
    broadcastFrequency: Optional[
        Union[BroadcastFrequencySpecification, List[BroadcastFrequencySpecification]]
    ] = None
