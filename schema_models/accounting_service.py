from dataclasses import dataclass

from schema_models.financial_service import FinancialService


@dataclass
class AccountingService(FinancialService):
    """
    Accountancy business.

    As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).

    """
