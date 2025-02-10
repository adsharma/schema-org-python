from typing import List, Optional, Union

from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class LendAction(TransferAction):
    """
    The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.

    Related actions:

    * [[BorrowAction]]: Reciprocal of LendAction.
    """

    borrower: Optional[Union[Person, List[Person]]] = None
