from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.place import Place


class ArchiveComponent(CreativeWork):
    itemLocation: Optional[Union[str, List[str]]] = None
    itemLocation: Optional[Union[Place, List[Place]]] = None
    itemLocation: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    holdingArchive: Optional[
        Union["ArchiveOrganization", List["ArchiveOrganization"]]
    ] = None
