from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.transfer_action import TransferAction


@dataclass
class MoneyTransfer(TransferAction):
    """
    The act of transferring money from one place to another place. This may occur electronically or physically.
    """

    amount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
    beneficiaryBank: Optional[
        Union["BankOrCreditUnion", List["BankOrCreditUnion"], str, List[str]]
    ] = None
