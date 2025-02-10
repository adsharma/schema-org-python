from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.place import Place


class MoveAction(Action):
    """
    The act of an agent relocating to a place.

    Related actions:

    * [[TransferAction]]: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.
    """

    fromLocation: Optional[Union[Place, List[Place]]] = None
    toLocation: Optional[Union[Place, List[Place]]] = None
