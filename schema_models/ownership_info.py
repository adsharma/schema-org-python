from datetime import datetime
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


class OwnershipInfo(StructuredValue):
    """
    A structured value providing information about when a certain organization or person owned a certain product.
    """

    ownedThrough: Optional[Union[datetime, List[datetime]]] = None
    acquiredFrom: Optional[Union[Person, List[Person]]] = None
    acquiredFrom: Optional[Union[Organization, List[Organization]]] = None
    ownedFrom: Optional[Union[datetime, List[datetime]]] = None
    typeOfGood: Optional[Union[Product, List[Product]]] = None
    typeOfGood: Optional[Union[Service, List[Service]]] = None
