from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.event import Event
from schema_models.language import Language
from schema_models.publication_event import PublicationEvent
from schema_models.text import Text


class BroadcastEvent(PublicationEvent):
    isLiveBroadcast: Optional[Union[Boolean, List[Boolean]]] = None
    broadcastOfEvent: Optional[Union[Event, List[Event]]] = None
    videoFormat: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Text, List[Text]]] = None
    subtitleLanguage: Optional[Union[Language, List[Language]]] = None
