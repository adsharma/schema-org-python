from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class MediaReviewItem(CreativeWork):
    mediaItemAppearance: Optional[Union[MediaObject, List[MediaObject]]] = None
