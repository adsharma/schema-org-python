from dataclasses import dataclass

from schema_models.visual_artwork import VisualArtwork


@dataclass
class CoverArt(VisualArtwork):
    """
    The artwork on the outer surface of a CreativeWork.
    """
