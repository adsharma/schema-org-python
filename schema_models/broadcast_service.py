from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.broadcast_channel import BroadcastChannel
from schema_models.broadcast_frequency_specification import (
    BroadcastFrequencySpecification,
)
from schema_models.broadcast_service import BroadcastService
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.service import Service
from schema_models.text import Text


class BroadcastService(Service):
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
    broadcaster: Optional[Union[Organization, List[Organization]]] = None
    area: Optional[Union[Place, List[Place]]] = None
    hasBroadcastChannel: Optional[Union[BroadcastChannel, List[BroadcastChannel]]] = (
        None
    )
    callSign: Optional[Union[Text, List[Text]]] = None
    videoFormat: Optional[Union[Text, List[Text]]] = None
    broadcastAffiliateOf: Optional[Union[Organization, List[Organization]]] = None
    parentService: Optional[Union["BroadcastService", List["BroadcastService"]]] = None
    broadcastDisplayName: Optional[Union[Text, List[Text]]] = None
    broadcastTimezone: Optional[Union[Text, List[Text]]] = None
    broadcastFrequency: Optional[Union[Text, List[Text]]] = None
    broadcastFrequency: Optional[
        Union[BroadcastFrequencySpecification, List[BroadcastFrequencySpecification]]
    ] = None
