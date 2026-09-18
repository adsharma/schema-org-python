from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.language import Language
from schema_models.publication_event import PublicationEvent


@dataclass
class BroadcastEvent(PublicationEvent):
    """
    An over the air or online broadcast event.
    """

    broadcastOfEvent: Optional[Union[Event, List[Event]]] = None
    isLiveBroadcast: Optional[Union[bool, List[bool]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    videoFormat: Optional[Union[str, List[str]]] = None
