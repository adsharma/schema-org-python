from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.business_function import BusinessFunction
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: Optional[Union[float, List[float]]] = None
    typeOfGood: Optional[Union[Product, List[Product]]] = None
    typeOfGood: Optional[Union[Service, List[Service]]] = None
    unitCode: Optional[Union[str, List[str]]] = None
    unitCode: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    unitText: Optional[Union[str, List[str]]] = None
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = None
