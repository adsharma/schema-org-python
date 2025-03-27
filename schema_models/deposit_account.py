from dataclasses import dataclass

from schema_models.bank_account import BankAccount


@dataclass
class DepositAccount(BankAccount):
    """
    A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.
    """
