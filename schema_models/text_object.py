from dataclasses import dataclass

from schema_models.media_object import MediaObject


@dataclass
class TextObject(MediaObject):
    """
    A text file. The text can be unformatted or contain markup, html, etc.
    """
