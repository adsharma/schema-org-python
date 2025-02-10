from typing import List, Optional, Union

from schema_models.consume_action import ConsumeAction
from schema_models.game_availability_enumeration import GameAvailabilityEnumeration


class PlayGameAction(ConsumeAction):
    """
    The act of playing a video game.
    """

    gameAvailabilityType: Optional[
        Union[GameAvailabilityEnumeration, List[GameAvailabilityEnumeration]]
    ] = None
    gameAvailabilityType: Optional[Union[str, List[str]]] = None
