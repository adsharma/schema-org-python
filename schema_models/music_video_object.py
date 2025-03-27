from dataclasses import dataclass

from schema_models.media_object import MediaObject


@dataclass
class MusicVideoObject(MediaObject):
    """
    A music video file.
    """
