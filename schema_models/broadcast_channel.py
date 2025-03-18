from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class BroadcastChannel(Intangible):
    """
    A unique instance of a BroadcastService on a CableOrSatelliteService lineup.
    """

    providesBroadcastService: Optional[
        Union["BroadcastService", List["BroadcastService"]]
    ] = None
    broadcastFrequency: Optional[
        Union[
            str,
            List[str],
            "BroadcastFrequencySpecification",
            List["BroadcastFrequencySpecification"],
        ]
    ] = None
    broadcastServiceTier: Optional[Union[str, List[str]]] = None
    inBroadcastLineup: Optional[
        Union["CableOrSatelliteService", List["CableOrSatelliteService"]]
    ] = None
    broadcastChannelId: Optional[Union[str, List[str]]] = None
    genre: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
