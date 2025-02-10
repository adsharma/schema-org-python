from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.transfer_action import TransferAction


class MoneyTransfer(TransferAction):
    """
    The act of transferring money from one place to another place. This may occur electronically or physically.
    """

    beneficiaryBank: Optional[Union[str, List[str]]] = None
    beneficiaryBank: Optional[Union["BankOrCreditUnion", List["BankOrCreditUnion"]]] = (
        None
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[float, List[float]]] = None
