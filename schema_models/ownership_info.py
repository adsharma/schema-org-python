from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


@dataclass
class OwnershipInfo(StructuredValue):
    """
    A structured value providing information about when a certain organization or person owned a certain product.
    """

    acquiredFrom: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    ownedFrom: Optional[Union[datetime, List[datetime]]] = None
    ownedThrough: Optional[Union[datetime, List[datetime]]] = None
    typeOfGood: Optional[Union[Product, List[Product], Service, List[Service]]] = None
