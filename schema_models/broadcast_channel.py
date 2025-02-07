from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class BroadcastChannel(Intangible):
    providesBroadcastService: Optional[
        Union["BroadcastService", List["BroadcastService"]]
    ] = None
    broadcastFrequency: Optional[Union[Text, List[Text]]] = None
    broadcastFrequency: Optional[
        Union[
            "BroadcastFrequencySpecification", List["BroadcastFrequencySpecification"]
        ]
    ] = None
    broadcastServiceTier: Optional[Union[Text, List[Text]]] = None
    inBroadcastLineup: Optional[
        Union["CableOrSatelliteService", List["CableOrSatelliteService"]]
    ] = None
    broadcastChannelId: Optional[Union[Text, List[Text]]] = None
    genre: Optional[Union[Text, List[Text]]] = None
    genre: Optional[Union[URL, List[URL]]] = None
