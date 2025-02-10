from typing import List, Optional, Union

from schema_models.role import Role


class OrganizationRole(Role):
    """
    A subclass of Role used to describe roles within organizations.
    """

    numberedPosition: Optional[Union[float, List[float]]] = None
