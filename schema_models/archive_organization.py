from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.archive_component import ArchiveComponent
from schema_models.local_business import LocalBusiness


class ArchiveOrganization(LocalBusiness):
    archiveHeld: Optional[Union[ArchiveComponent, List[ArchiveComponent]]] = None
