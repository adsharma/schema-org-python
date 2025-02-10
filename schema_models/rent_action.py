from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


class RentAction(TradeAction):
    """
    The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.
    """

    realEstateAgent: Optional[Union["RealEstateAgent", List["RealEstateAgent"]]] = None
    landlord: Optional[Union[Person, List[Person]]] = None
    landlord: Optional[Union[Organization, List[Organization]]] = None
