from typing import List, Optional, Union

from schema_models.language import Language
from schema_models.role import Role
from schema_models.text import Text


class LinkRole(Role):
    linkRelationship: Optional[Union[Text, List[Text]]] = None
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
