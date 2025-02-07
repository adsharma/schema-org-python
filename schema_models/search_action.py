from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.text import Text


class SearchAction(Action):
    query: Optional[Union[Text, List[Text]]] = None
