from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


class DigitalDocumentPermission(Intangible):
    permissionType: Optional[
        Union["DigitalDocumentPermissionType", List["DigitalDocumentPermissionType"]]
    ] = None
    grantee: Optional[Union[Person, List[Person]]] = None
    grantee: Optional[Union[Organization, List[Organization]]] = None
    grantee: Optional[Union["Audience", List["Audience"]]] = None
    grantee: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
