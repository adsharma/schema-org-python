from dataclasses import dataclass

from schema_models.media_gallery import MediaGallery


@dataclass
class VideoGallery(MediaGallery):
    """
    Web page type: Video gallery page.
    """
