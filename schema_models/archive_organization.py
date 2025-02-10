from typing import List, Optional, Union

from schema_models.archive_component import ArchiveComponent
from schema_models.local_business import LocalBusiness


class ArchiveOrganization(LocalBusiness):
    """
    An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.
    """

    archiveHeld: Optional[Union[ArchiveComponent, List[ArchiveComponent]]] = None
