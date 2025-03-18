from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class GeoCoordinates(StructuredValue):
    """
    The geographic coordinates of a place or event.
    """

    addressCountry: Optional[Union[str, List[str], "Country", List["Country"]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = (
        None
    )
    elevation: Optional[Union[str, List[str], float, List[float]]] = None
    longitude: Optional[Union[float, List[float], str, List[str]]] = None
    latitude: Optional[Union[str, List[str], float, List[float]]] = None
