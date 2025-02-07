from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.text import Text
from schema_models.transfer_action import TransferAction


class MoneyTransfer(TransferAction):
    beneficiaryBank: Optional[Union[Text, List[Text]]] = None
    beneficiaryBank: Optional[Union["BankOrCreditUnion", List["BankOrCreditUnion"]]] = (
        None
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    amount: Optional[Union[Number, List[Number]]] = None
