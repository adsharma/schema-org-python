from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class GeoShape(StructuredValue):
    box: Optional[Union[str, List[str]]] = None
    address: Optional[Union[str, List[str]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    circle: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union["Country", List["Country"]]] = None
    line: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    elevation: Optional[Union[str, List[str]]] = None
    elevation: Optional[Union[float, List[float]]] = None
    polygon: Optional[Union[str, List[str]]] = None
