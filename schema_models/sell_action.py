from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction
from schema_models.warranty_promise import WarrantyPromise


class SellAction(TradeAction):
    """
    The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.
    """

    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    buyer: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
