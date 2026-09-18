from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


@dataclass
class GeoCoordinates(StructuredValue):
    """
    The geographic coordinates of a place or event.
    """

    address: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str]]] = (
        None
    )
    addressCountry: Optional[Union["Country", List["Country"], str, List[str]]] = None
    elevation: Optional[Union[float, List[float], str, List[str]]] = None
    latitude: Optional[Union[float, List[float], str, List[str]]] = None
    longitude: Optional[Union[float, List[float], str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
