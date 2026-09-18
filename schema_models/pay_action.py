from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


@dataclass
class PayAction(TradeAction):
    """
    An agent pays a price to a participant.
    """

    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
