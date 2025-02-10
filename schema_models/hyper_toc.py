from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.media_object import MediaObject


class HyperToc(CreativeWork):
    """
    A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items.
    """

    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    tocEntry: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
