from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.archive_organization import ArchiveOrganization
from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.text import Text


class ArchiveComponent(CreativeWork):
    itemLocation: Optional[Union[Text, List[Text]]] = None
    itemLocation: Optional[Union[Place, List[Place]]] = None
    itemLocation: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    holdingArchive: Optional[Union[ArchiveOrganization, List[ArchiveOrganization]]] = (
        None
    )
