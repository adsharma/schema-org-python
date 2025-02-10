from typing import List, Optional, Union

from schema_models.create_action import CreateAction
from schema_models.language import Language


class WriteAction(CreateAction):
    """
    The act of authoring written creative content.
    """

    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    language: Optional[Union[Language, List[Language]]] = None
