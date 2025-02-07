from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.text import Text


class ArchiveComponent(CreativeWork):
    itemLocation: Optional[Union[Text, List[Text]]] = None
    itemLocation: Optional[Union[Place, List[Place]]] = None
    itemLocation: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    holdingArchive: Optional[
        Union["ArchiveOrganization", List["ArchiveOrganization"]]
    ] = None
