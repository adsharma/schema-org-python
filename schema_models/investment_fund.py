from dataclasses import dataclass

from schema_models.investment_or_deposit import InvestmentOrDeposit


@dataclass
class InvestmentFund(InvestmentOrDeposit):
    """
    A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.
    """
