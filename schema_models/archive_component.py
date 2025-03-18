from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.place import Place


class ArchiveComponent(CreativeWork):
    """
    An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.
    """

    itemLocation: Optional[
        Union[
            str, List[str], Place, List[Place], "PostalAddress", List["PostalAddress"]
        ]
    ] = None
    holdingArchive: Optional[
        Union["ArchiveOrganization", List["ArchiveOrganization"]]
    ] = None
