from typing import List, Optional, Union

from schema_models.create_action import CreateAction
from schema_models.language import Language
from schema_models.text import Text


class WriteAction(CreateAction):
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
    language: Optional[Union[Language, List[Language]]] = None
