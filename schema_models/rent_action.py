from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


@dataclass
class RentAction(TradeAction):
    """
    The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.
    """

    landlord: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    realEstateAgent: Optional[Union["RealEstateAgent", List["RealEstateAgent"]]] = None
