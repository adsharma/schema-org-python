from typing import List, Optional, Union

from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class LendAction(TransferAction):
    borrower: Optional[Union[Person, List[Person]]] = None
