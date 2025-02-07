from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


class OwnershipInfo(StructuredValue):
    ownedThrough: Optional[Union[DateTime, List[DateTime]]] = None
    acquiredFrom: Optional[Union[Person, List[Person]]] = None
    acquiredFrom: Optional[Union[Organization, List[Organization]]] = None
    ownedFrom: Optional[Union[DateTime, List[DateTime]]] = None
    typeOfGood: Optional[Union[Product, List[Product]]] = None
    typeOfGood: Optional[Union[Service, List[Service]]] = None
