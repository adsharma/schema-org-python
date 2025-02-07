from typing import List, Optional, Union

from schema_models.country import Country
from schema_models.number import Number
from schema_models.postal_address import PostalAddress
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class GeoShape(StructuredValue):
    box: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    circle: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Country, List[Country]]] = None
    line: Optional[Union[Text, List[Text]]] = None
    postalCode: Optional[Union[Text, List[Text]]] = None
    elevation: Optional[Union[Text, List[Text]]] = None
    elevation: Optional[Union[Number, List[Number]]] = None
    polygon: Optional[Union[Text, List[Text]]] = None
