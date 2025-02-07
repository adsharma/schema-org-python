from typing import List, Optional, Union

from schema_models.number import Number
from schema_models.role import Role


class OrganizationRole(Role):
    numberedPosition: Optional[Union[Number, List[Number]]] = None
