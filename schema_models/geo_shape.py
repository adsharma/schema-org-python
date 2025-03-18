from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class GeoShape(StructuredValue):
    """
    The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.
    """

    box: Optional[Union[str, List[str]]] = None
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = (
        None
    )
    circle: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[str, List[str], "Country", List["Country"]]] = None
    line: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    elevation: Optional[Union[str, List[str], float, List[float]]] = None
    polygon: Optional[Union[str, List[str]]] = None
