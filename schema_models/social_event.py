from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class SocialEvent(Event):
    """
    Event type: Social event.
    """
