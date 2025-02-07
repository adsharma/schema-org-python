from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.investment_or_deposit import InvestmentOrDeposit


class BrokerageAccount(InvestmentOrDeposit):
    pass
