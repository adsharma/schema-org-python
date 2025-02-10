from typing import List, Optional, Union

from schema_models.distance import Distance
from schema_models.move_action import MoveAction


class TravelAction(MoveAction):
    """
    The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.
    """

    distance: Optional[Union[Distance, List[Distance]]] = None
