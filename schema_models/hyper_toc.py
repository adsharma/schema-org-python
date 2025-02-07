from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.hyper_toc_entry import HyperTocEntry
from schema_models.media_object import MediaObject


class HyperToc(CreativeWork):
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    tocEntry: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = None
