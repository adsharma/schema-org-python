from dataclasses import dataclass

from schema_models.media_object import MediaObject


@dataclass
class AmpStory(MediaObject):
    """
    A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
