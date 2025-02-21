from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class HyperTocEntry(CreativeWork):
    """
    A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].
    """

    utterances: Optional[Union[str, List[str]]] = None
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    tocContinuation: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
