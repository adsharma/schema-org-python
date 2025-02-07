from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.country import Country
from schema_models.number import Number
from schema_models.postal_address import PostalAddress
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class GeoCoordinates(StructuredValue):
    addressCountry: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Country, List[Country]]] = None
    postalCode: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    elevation: Optional[Union[Text, List[Text]]] = None
    elevation: Optional[Union[Number, List[Number]]] = None
    longitude: Optional[Union[Number, List[Number]]] = None
    longitude: Optional[Union[Text, List[Text]]] = None
    latitude: Optional[Union[Text, List[Text]]] = None
    latitude: Optional[Union[Number, List[Number]]] = None
