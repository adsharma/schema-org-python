from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.business_function import BusinessFunction
from schema_models.number import Number
from schema_models.product import Product
from schema_models.service import Service
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.url import URL


class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: Optional[Union[Number, List[Number]]] = None
    typeOfGood: Optional[Union[Product, List[Product]]] = None
    typeOfGood: Optional[Union[Service, List[Service]]] = None
    unitCode: Optional[Union[Text, List[Text]]] = None
    unitCode: Optional[Union[URL, List[URL]]] = None
    unitText: Optional[Union[Text, List[Text]]] = None
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = None
