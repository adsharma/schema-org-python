from typing import List, Optional, Union

from schema_models.role import Role


class PerformanceRole(Role):
    """
    A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.
    """

    characterName: Optional[Union[str, List[str]]] = None
