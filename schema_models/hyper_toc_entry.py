from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class HyperTocEntry(CreativeWork):
    utterances: Optional[Union[str, List[str]]] = None
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    tocContinuation: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
