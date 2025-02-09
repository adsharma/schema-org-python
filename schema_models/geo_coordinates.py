from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class GeoCoordinates(StructuredValue):
    addressCountry: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union["Country", List["Country"]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    address: Optional[Union[str, List[str]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    elevation: Optional[Union[str, List[str]]] = None
    elevation: Optional[Union[float, List[float]]] = None
    longitude: Optional[Union[float, List[float]]] = None
    longitude: Optional[Union[str, List[str]]] = None
    latitude: Optional[Union[str, List[str]]] = None
    latitude: Optional[Union[float, List[float]]] = None
