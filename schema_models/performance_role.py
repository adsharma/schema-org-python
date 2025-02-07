from typing import List, Optional, Union

from schema_models.role import Role
from schema_models.text import Text


class PerformanceRole(Role):
    characterName: Optional[Union[Text, List[Text]]] = None
