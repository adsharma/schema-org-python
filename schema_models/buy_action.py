from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trade_action import TradeAction
from schema_models.warranty_promise import WarrantyPromise


class BuyAction(TradeAction):
    warrantyPromise: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    vendor: Optional[Union[Person, List[Person]]] = None
    vendor: Optional[Union[Organization, List[Organization]]] = None
