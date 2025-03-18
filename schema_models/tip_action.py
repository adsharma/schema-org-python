from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


class TipAction(TradeAction):
    """
    The act of giving money voluntarily to a beneficiary in recognition of services rendered.
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
