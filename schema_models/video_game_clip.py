from dataclasses import dataclass

from schema_models.clip import Clip


@dataclass
class VideoGameClip(Clip):
    """
    A short segment/part of a video game.
    """
