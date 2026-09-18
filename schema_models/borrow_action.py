from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


@dataclass
class BorrowAction(TransferAction):
    """
    The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.

    Related actions:

    * [[LendAction]]: Reciprocal of BorrowAction.
    """

    lender: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
