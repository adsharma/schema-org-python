from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction


@dataclass
class BuyAction(TradeAction):
    """
    The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.
    """

    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    vendor: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    warrantyPromise: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
