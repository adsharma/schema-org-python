from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class BorrowAction(TransferAction):
    lender: Optional[Union[Person, List[Person]]] = None
    lender: Optional[Union[Organization, List[Organization]]] = None
