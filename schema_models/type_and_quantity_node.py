from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.business_function import BusinessFunction
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    """
    A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.
    """

    amountOfThisGood: Optional[Union[float, List[float]]] = None
    typeOfGood: Optional[Union[Product, List[Product], Service, List[Service]]] = None
    unitCode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    unitText: Optional[Union[str, List[str]]] = None
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = None
