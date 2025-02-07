from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction
from schema_models.warranty_promise import WarrantyPromise


class SellAction(TradeAction):
    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    buyer: Optional[Union[Organization, List[Organization]]] = None
    buyer: Optional[Union[Person, List[Person]]] = None
