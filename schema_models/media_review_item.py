from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class MediaReviewItem(CreativeWork):
    mediaItemAppearance: Optional[Union[MediaObject, List[MediaObject]]] = None
