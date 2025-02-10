from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.place import Place


class TransferAction(Action):
    """
    The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.
    """

    toLocation: Optional[Union[Place, List[Place]]] = None
    fromLocation: Optional[Union[Place, List[Place]]] = None
