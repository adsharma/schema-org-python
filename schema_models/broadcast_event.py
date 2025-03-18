from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.language import Language
from schema_models.publication_event import PublicationEvent


class BroadcastEvent(PublicationEvent):
    """
    An over the air or online broadcast event.
    """

    isLiveBroadcast: Optional[Union[bool, List[bool]]] = None
    broadcastOfEvent: Optional[Union[Event, List[Event]]] = None
    videoFormat: Optional[Union[str, List[str]]] = None
    subtitleLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
