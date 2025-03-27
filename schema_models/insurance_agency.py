from dataclasses import dataclass

from schema_models.financial_service import FinancialService


@dataclass
class InsuranceAgency(FinancialService):
    """
    An Insurance agency.
    """
