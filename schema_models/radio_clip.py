from dataclasses import dataclass

from schema_models.clip import Clip


@dataclass
class RadioClip(Clip):
    """
    A short radio program or a segment/part of a radio program.
    """
