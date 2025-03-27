from dataclasses import dataclass

from schema_models.financial_service import FinancialService


@dataclass
class BankOrCreditUnion(FinancialService):
    """
    Bank or credit union.
    """
