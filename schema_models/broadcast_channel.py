from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class BroadcastChannel(Intangible):
    providesBroadcastService: Optional[
        Union["BroadcastService", List["BroadcastService"]]
    ] = None
    broadcastFrequency: Optional[Union[str, List[str]]] = None
    broadcastFrequency: Optional[
        Union[
            "BroadcastFrequencySpecification", List["BroadcastFrequencySpecification"]
        ]
    ] = None
    broadcastServiceTier: Optional[Union[str, List[str]]] = None
    inBroadcastLineup: Optional[
        Union["CableOrSatelliteService", List["CableOrSatelliteService"]]
    ] = None
    broadcastChannelId: Optional[Union[str, List[str]]] = None
    genre: Optional[Union[str, List[str]]] = None
    genre: Optional[Union[HttpUrl, List[HttpUrl]]] = None
