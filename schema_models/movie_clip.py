from dataclasses import dataclass

from schema_models.clip import Clip


@dataclass
class MovieClip(Clip):
    """
    A short segment/part of a movie.
    """
