from typing import List, Optional, Union

from schema_models.thing import Thing
from schema_models.update_action import UpdateAction


class ReplaceAction(UpdateAction):
    """
    The act of editing a recipient by replacing an old object with a new object.
    """

    replacee: Optional[Union[Thing, List[Thing]]] = None
    replacer: Optional[Union[Thing, List[Thing]]] = None
