from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class DigitalDocumentPermission(Intangible):
    """
    A permission for a particular person or group to access a particular file.
    """

    grantee: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
    permissionType: Optional[
        Union["DigitalDocumentPermissionType", List["DigitalDocumentPermissionType"]]
    ] = None
