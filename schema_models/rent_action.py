from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.real_estate_agent import RealEstateAgent
from schema_models.trade_action import TradeAction


class RentAction(TradeAction):
    realEstateAgent: Optional[Union[RealEstateAgent, List[RealEstateAgent]]] = None
    landlord: Optional[Union[Person, List[Person]]] = None
    landlord: Optional[Union[Organization, List[Organization]]] = None
