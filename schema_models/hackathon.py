from dataclasses import dataclass

from schema_models.event import Event


@dataclass
class Hackathon(Event):
    """
    A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
