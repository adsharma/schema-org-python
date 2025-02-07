from typing import List, Optional, Union

from schema_models.grant import Grant
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person


class MonetaryGrant(Grant):
    amount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    amount: Optional[Union[Number, List[Number]]] = None
    funder: Optional[Union[Person, List[Person]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
