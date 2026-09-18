from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class IncentiveType(Enumeration):
    """
    The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies, etc.).
    """
