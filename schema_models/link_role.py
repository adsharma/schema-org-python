from typing import List, Optional, Union

from schema_models.language import Language
from schema_models.role import Role


class LinkRole(Role):
    linkRelationship: Optional[Union[str, List[str]]] = None
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
