from typing import List, Optional, Union

from schema_models.action import Action


class SearchAction(Action):
    query: Optional[Union[str, List[str]]] = None
