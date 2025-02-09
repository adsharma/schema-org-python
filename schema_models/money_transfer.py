from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.transfer_action import TransferAction


class MoneyTransfer(TransferAction):
    beneficiaryBank: Optional[Union[str, List[str]]] = None
    beneficiaryBank: Optional[Union["BankOrCreditUnion", List["BankOrCreditUnion"]]] = (
        None
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[float, List[float]]] = None
