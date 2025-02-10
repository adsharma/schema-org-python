from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.thing import Thing


class UpdateAction(Action):
    """
    The act of managing by changing/editing the state of the object.
    """

    collection: Optional[Union[Thing, List[Thing]]] = None
    targetCollection: Optional[Union[Thing, List[Thing]]] = None
