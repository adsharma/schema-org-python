from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MusicReleaseFormatType(Enumeration):
    """
    Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
    """
