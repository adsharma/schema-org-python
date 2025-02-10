from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.audience import Audience
from schema_models.event import Event


class PlayAction(Action):
    """
    The act of playing/exercising/training/performing for enjoyment, leisure, recreation, competition or exercise.

    Related actions:

    * [[ListenAction]]: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.
    * [[WatchAction]]: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content.
    """

    event: Optional[Union[Event, List[Event]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
