from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boarding_policy_type import BoardingPolicyType
from schema_models.organization import Organization
from schema_models.text import Text


class Airline(Organization):
    iataCode: Optional[Union[Text, List[Text]]] = None
    boardingPolicy: Optional[Union[BoardingPolicyType, List[BoardingPolicyType]]] = None
