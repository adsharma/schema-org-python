from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.consume_action import ConsumeAction


@dataclass
class PlayGameAction(ConsumeAction):
    """
    The act of playing a video game.
    """

    gameAvailabilityType: Optional[
        Union[
            "GameAvailabilityEnumeration",
            List["GameAvailabilityEnumeration"],
            str,
            List[str],
        ]
    ] = None
