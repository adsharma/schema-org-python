from typing import List, Optional, Union

from schema_models.role import Role


class PerformanceRole(Role):
    characterName: Optional[Union[str, List[str]]] = None
