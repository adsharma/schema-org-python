from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


@dataclass
class BroadcastChannel(Intangible):
    """
    A unique instance of a BroadcastService on a CableOrSatelliteService lineup.
    """

    broadcastChannelId: Optional[Union[str, List[str]]] = None
    broadcastFrequency: Optional[
        Union[
            "BroadcastFrequencySpecification",
            List["BroadcastFrequencySpecification"],
            str,
            List[str],
        ]
    ] = None
    broadcastServiceTier: Optional[Union[str, List[str]]] = None
    genre: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    inBroadcastLineup: Optional[
        Union["CableOrSatelliteService", List["CableOrSatelliteService"]]
    ] = None
    providesBroadcastService: Optional[
        Union["BroadcastService", List["BroadcastService"]]
    ] = None
