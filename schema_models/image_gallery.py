from dataclasses import dataclass

from schema_models.media_gallery import MediaGallery


@dataclass
class ImageGallery(MediaGallery):
    """
    Web page type: Image gallery page.
    """
