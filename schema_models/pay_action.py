from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


class PayAction(TradeAction):
    """
    An agent pays a price to a participant.
    """

    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            ContactPoint,
            List[ContactPoint],
            Person,
            List[Person],
            Organization,
            List[Organization],
        ]
    ] = None
