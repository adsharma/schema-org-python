from dataclasses import dataclass

from schema_models.financial_product import FinancialProduct


@dataclass
class CurrencyConversionService(FinancialProduct):
    """
    A service to convert funds from one currency to another currency.
    """
