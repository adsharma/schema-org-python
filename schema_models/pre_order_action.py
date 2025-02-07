from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.trade_action import TradeAction


class PreOrderAction(TradeAction):
    pass
