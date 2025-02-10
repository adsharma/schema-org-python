from typing import List, Optional, Union

from schema_models.action import Action


class SearchAction(Action):
    """
    The act of searching for an object.

    Related actions:

    * [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.
    """

    query: Optional[Union[str, List[str]]] = None
