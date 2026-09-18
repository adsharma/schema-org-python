from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class IncentiveQualifiedExpenseType(Enumeration):
    """
    The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    """
