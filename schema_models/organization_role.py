from typing import List, Optional, Union

from schema_models.role import Role


class OrganizationRole(Role):
    numberedPosition: Optional[Union[float, List[float]]] = None
