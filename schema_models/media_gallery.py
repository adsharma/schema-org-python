from dataclasses import dataclass

from schema_models.collection_page import CollectionPage


@dataclass
class MediaGallery(CollectionPage):
    """
    Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia.
    """
