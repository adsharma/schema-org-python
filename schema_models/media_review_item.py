from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class MediaReviewItem(CreativeWork):
    """
    Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party.
    """

    mediaItemAppearance: Optional[Union[MediaObject, List[MediaObject]]] = None
