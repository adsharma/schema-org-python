from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


@dataclass
class GeoShape(StructuredValue):
    """
    The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.
    """

    address: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str]]] = (
        None
    )
    addressCountry: Optional[Union["Country", List["Country"], str, List[str]]] = None
    box: Optional[Union[str, List[str]]] = None
    circle: Optional[Union[str, List[str]]] = None
    elevation: Optional[Union[float, List[float], str, List[str]]] = None
    line: Optional[Union[str, List[str]]] = None
    polygon: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
