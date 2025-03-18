from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction
from schema_models.warranty_promise import WarrantyPromise


class BuyAction(TradeAction):
    """
    The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.
    """

    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    seller: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    vendor: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
