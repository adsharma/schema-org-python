from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


class DigitalDocumentPermission(Intangible):
    """
    A permission for a particular person or group to access a particular file.
    """

    permissionType: Optional[
        Union["DigitalDocumentPermissionType", List["DigitalDocumentPermissionType"]]
    ] = None
    grantee: Optional[
        Union[
            Person,
            List[Person],
            Organization,
            List[Organization],
            "Audience",
            List["Audience"],
            "ContactPoint",
            List["ContactPoint"],
        ]
    ] = None
